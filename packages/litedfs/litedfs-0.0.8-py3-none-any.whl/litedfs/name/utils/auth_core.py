# -*- coding: utf-8 -*-

import os
import json
import time
import random
import base64
import shutil
import logging
import datetime
from copy import deepcopy

from tornado import gen, ioloop
from tea_encrypt import EncryptStr, DecryptStr

from litedfs.name.utils.append_log import AppendLogJson
from litedfs.name.utils.listener import Connection
from litedfs.name.utils.common import md5sum, new_id, Errors, splitall
from litedfs.name.utils.common import InvalidValueError, SameNameExistsError, UserNotExistsError
from litedfs.name.utils.common import GroupNotExistsError, RecoverFailedError
from litedfs.name.config import CONFIG

LOG = logging.getLogger(__name__)


class I(object):
    info = "i"
    data = "d"
    cmd = "c"
    new_name = "n"
    target_path = "t"
    id = "id"
    uid = "uid"
    gid = "gid"
    default_group = "everyone"
    unknown_user = "unknown"
    unknown_group = "unknown"


class C(object):
    create_user = "cu"
    update_user = "uu"
    create_group = "cg"
    update_group = "ug"
    add_group_user = "agu"
    remove_group_user = "rgu"
    delete_user = "du"
    delete_group = "dg"


class AuthSystem(object):
    _instance = None
    name = "auth_system"

    def __new__(cls, interval = 10):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            cls._instance.users = {"unknown": {"name": "unknown"}}
            cls._instance.user_names = {"unknown": True}
            cls._instance.user_groups = {}
            cls._instance.groups = {"everyone": {"id": "everyone", "name": "everyone", "users": []}}
            cls._instance.group_names = {"everyone": True}
            cls._instance.editlog = None
            cls._instance.status = "booting"
            cls._instance.locks = {}
            cls._instance.interval = interval
        return cls._instance

    @classmethod
    def instance(cls):
        if cls._instance and cls._instance.status == "ready":
            return cls._instance
        else:
            return None

    @gen.coroutine
    def recover_coroutine(self):
        self.status = "recovering"
        success = yield self.backup_image_coroutine()
        if success:
            success = yield self.load_image_coroutine()
            if success:
                success = yield self.load_editlog_coroutine()
                if success:
                    success = yield self.dump_image_coroutine()
                    if success:
                        self.editlog = AppendLogJson(os.path.join(CONFIG["data_path"], "auth_editlog"))
                        self.status = "ready"
                    else:
                        raise RecoverFailedError("dump auth_image failed")
                else:
                    raise RecoverFailedError("load auth_editlog failed")
            else:
                raise RecoverFailedError("load auth_image failed")
        else:
            raise RecoverFailedError("backup auth_image failed")

    def recover(self):
        self.status = "recovering"
        success = self.backup_image()
        if success:
            success = self.load_image()
            if success:
                success = self.load_editlog()
                if success:
                    success = self.dump_image()
                    if success:
                        self.editlog = AppendLogJson(os.path.join(CONFIG["data_path"], "auth_editlog"))
                        self.status = "ready"
                    else:
                        raise RecoverFailedError("dump auth_image failed")
                else:
                    raise RecoverFailedError("load auth_editlog failed")
            else:
                raise RecoverFailedError("load auth_image failed")
        else:
            raise RecoverFailedError("backup auth_image failed")

    def add_user_group(self, uid, gid):
        if uid not in self.user_groups:
            self.user_groups[uid] = {}
        if uid in self.users:
            if gid in self.groups:
                self.user_groups[uid][gid] = True

    def remove_user_group(self, uid, gid):
        if uid not in self.user_groups:
            self.user_groups[uid] = {}
        if gid in self.user_groups[uid]:
            del self.user_groups[uid][gid]

    def create_user(self, name, password, email = "", phone = "", uid = None, ctime = None, mtime = None, recover = False):
        result = False
        now = int(time.time())
        if name not in self.user_names:
            user = {
                "id": uid if uid else new_id(),
                "name": name,
                "password": password if recover else md5sum(password),
                "email": email,
                "phone": phone,
                "ctime": ctime if ctime else now,
                "mtime": mtime if mtime else now,
            }
            self.users[user["id"]] = user
            self.user_names[user["name"]] = user["id"]
            if self.editlog:
                self.editlog.writeline({I.cmd: C.create_user, I.info: user})
            result = True
        else:
            raise SameNameExistsError("same user name exists: %s" % name)
        return result

    def update_user(self, uid, data = {}, recover = False):
        result = False
        now = int(time.time())
        if "mtime" in data:
            now = data["mtime"]
        if uid in self.users:
            if "name" in data:
                if (data["name"] not in self.user_names) or (data["name"] in self.user_names and self.user_names[data["name"]] == uid):
                    del self.user_names[self.users[uid]["name"]]
                    self.user_names[data["name"]] = uid
                    self.users[uid]["name"] = data["name"]
                else:
                    raise SameNameExistsError("same user name exists: %s" % data["name"])
            if "password" in data:
                if not recover:
                    data["password"] = md5sum(data["password"])
                self.users[uid]["password"] = data["password"]
            if "email" in data:
                self.users[uid]["email"] = data["email"]
            if "phone" in data:
                self.users[uid]["phone"] = data["phone"]
            self.users[uid]["mtime"] = now
            data["mtime"] = now
            if self.editlog:
                self.editlog.writeline({I.cmd: C.update_user, I.uid: uid, I.data: data})
            result = True
        else:
            raise UserNotExistsError("user not exists: %s" % uid)
        return result

    def create_group(self, name, owner, users = None, gid = None, ctime = None, mtime = None):
        result = False
        now = int(time.time())
        if name not in self.group_names:
            if owner in self.users:
                if gid is None:
                    gid = new_id()
                if users is None:
                    users = {owner: True}
                group = {
                    "id": gid,
                    "name": name,
                    "owner": owner,
                    "users": users,
                    "ctime": ctime if ctime else now,
                    "mtime": mtime if mtime else now,
                }
                if owner:
                    self.add_user_group(owner, gid)
                for uid in users:
                    self.add_user_group(uid, gid)
                self.groups[group["id"]] = group
                self.group_names[group["name"]] = group["id"]
                if self.editlog:
                    self.editlog.writeline({I.cmd: C.create_group, I.info: group})
                result = True
            else:
                raise UserNotExistsError("user not exists: %s" % owner)
        else:
            raise SameNameExistsError("same group name exists: %s" % name)
        return result

    def update_group(self, gid, data = {}):
        result = False
        now = int(time.time())
        if "mtime" in data:
            now = data["mtime"]
        if gid in self.groups:
            if "name" in data:
                if (data["name"] not in self.group_names) or (data["name"] in self.group_names and self.group_names[data["name"]] == gid):
                    del self.group_names[self.groups[gid]["name"]]
                    self.group_names[data["name"]] = gid
                    self.groups[gid]["name"] = data["name"]
                else:
                    raise SameNameExistsError("same group name exists: %s" % data["name"])
            if "owner" in data:
                if data["owner"] in self.users:
                    self.groups[gid]["owner"] = data["owner"]
                    self.groups[gid]["users"][data["owner"]] = True
                    self.add_user_group(data["owner"], gid)
                else:
                    raise UserNotExistsError("user not exists: %s" % owner)
            self.groups[gid]["mtime"] = now
            data["mtime"] = now
            if self.editlog:
                self.editlog.writeline({I.cmd: C.update_group, I.gid: gid, I.data: data})
            result = True
        else:
            raise GroupNotExistsError("group not exists: %s" % gid)
        return result

    def delete_user(self, uid):
        result = True
        if uid in self.users:
            name = self.users[uid]["name"]
            del self.user_names[name]
            del self.users[uid]
            if uid in self.user_groups:
                del self.user_groups[uid]
            for gid in self.groups:
                if uid in self.groups[gid]["users"]:
                    del self.groups[gid]["users"][uid]
            if self.editlog:
                self.editlog.writeline({I.cmd: C.delete_user, I.uid: uid})
            result = True
        else:
            result = True
        return result

    def delete_group(self, gid):
        result = True
        if gid in self.groups:
            name = self.groups[gid]["name"]
            del self.group_names[name]
            del self.groups[gid]
            for uid in self.user_groups:
                if gid in self.user_groups[uid]:
                    del self.user_groups[uid][gid]
            if self.editlog:
                self.editlog.writeline({I.cmd: C.delete_group, I.gid: gid})
            result = True
        else:
            result = True
        return result

    def add_group_user(self, gid, uid):
        result = True
        if gid in self.groups:
            if uid in self.users:
                self.groups[gid]["users"][uid] = True
                self.add_user_group(uid, gid)
                if self.editlog:
                    self.editlog.writeline({I.cmd: C.add_group_user, I.gid: gid, I.uid: uid})
                result = True
            else:
                raise UserNotExistsError("user not exists: %s" % uid)
        else:
            raise GroupNotExistsError("group not exists: %s" % gid)
        return result

    def remove_group_user(self, gid, uid):
        result = True
        if gid in self.groups:
            if uid in self.groups[gid]["users"]:
                del self.groups[gid]["users"][uid]
                self.remove_user_group(uid, gid)
                if self.editlog:
                    self.editlog.writeline({I.cmd: C.remove_group_user, I.gid: gid, I.uid: uid})
                result = True
            else:
                raise UserNotExistsError("user not exists: %s" % uid)
        else:
            raise GroupNotExistsError("group not exists: %s" % gid)
        return result

    def info_user(self, uid, password = False):
        result = False
        if uid in self.users:
            user = self.users[uid]
            tmp = {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "phone": user["phone"],
            }
            if password:
                tmp["password"] = user["password"]
            result = tmp
        else:
            raise UserNotExistsError("user not exists: %s" % uid)
        return result

    def is_valid_user(self, name, password):
        result = False
        try:
            if name in self.user_names:
                user = self.users[self.user_names[name]]
                if user["password"] == md5sum(password):
                    result = {
                        "id": user["id"],
                        "name": user["name"],
                    }
        except Exception as e:
            LOG.exception(e)
        return result

    def generate_user_token(self, uid, expiration = 3600):
        result = False
        if uid in self.users:
            now = int(time.time())
            user = self.users[uid]
            content = "%s:%s:%s:%s" % (user["id"], user["name"], user["password"], now + expiration)
            result = base64.b64encode(EncryptStr(content.encode("utf-8"), CONFIG["token_key"])).decode()
        else:
            raise UserNotExistsError("user not exists: %s" % uid)
        return result

    def verify_user_token(self, token):
        result = False
        now = int(time.time())
        try:
            if isinstance(token, str):
                token = token.encode("utf-8")
            content = DecryptStr(base64.b64decode(token), CONFIG["token_key"].encode("utf-8"))
            uid, name, password, expired_at = content.decode("utf-8").split(":")
            expired_at = int(expired_at)
            if now < expired_at and uid in self.users and self.users[uid]["password"] == password:
                result = {
                    "id": self.users[uid]["id"],
                    "name": self.users[uid]["name"],
                }
        except Exception as e:
            LOG.exception(e)
        return result

    def info_group(self, gid):
        result = False
        if gid in self.groups:
            result = self.groups[gid]
        else:
            raise GroupNotExistsError("group not exists: %s" % gid)
        return result

    def is_group_owner(self, gid, uid, raise_error = False):
        result = False
        if gid in self.groups:
            if uid == self.groups[gid]["owner"]:
                result = True
        else:
            if raise_error:
                raise GroupNotExistsError("group not exists: %s" % gid)
        return result

    def is_group_user(self, gid, uid, raise_error = False):
        result = False
        if gid in self.groups:
            for u in self.groups[gid]["users"]:
                if u == uid:
                    result = True
                    break
        else:
            if raise_error:
                raise GroupNotExistsError("group not exists: %s" % gid)
        return result

    def is_admin(self, uid):
        result = False
        if uid == "admin":
            result = True
        return result

    def list_users(self, gid = "everyone", password = False):
        result = []
        if gid == "everyone":
            for uid in self.users:
                if uid != "unknown":
                    user = self.users[uid]
                    tmp = {
                        "id": user["id"],
                        "name": user["name"],
                        "email": user["email"],
                        "phone": user["phone"],
                        "ctime": user["ctime"],
                        "mtime": user["mtime"],
                    }
                    if password:
                        tmp["password"] = user["password"]
                    result.append(tmp)
        elif gid in self.groups:
            for uid in self.groups[gid]["users"]:
                if uid in self.users:
                    user = self.users[uid]
                    tmp = {
                        "id": user["id"],
                        "name": user["name"],
                        "email": user["email"],
                        "phone": user["phone"],
                        "ctime": user["ctime"],
                        "mtime": user["mtime"],
                    }
                    if password:
                        tmp["password"] = user["password"]
                    result.append(tmp)
        return result

    def list_groups(self):
        result = []
        for gid in self.groups:
            if gid != "everyone":
                result.append(self.groups[gid])
        return result

    def valid_user_name(self, name):
        result = False
        if name not in self.user_names:
            result = True
        return result

    def valid_group_name(self, name):
        result = False
        if name not in self.group_names:
            result = True
        return result

    @gen.coroutine
    def load_image_coroutine(self):
        result = self.load_image()
        raise gen.Return(result)

    @gen.coroutine
    def load_editlog_coroutine(self):
        result = self.load_editlog()
        raise gen.Return(result)

    @gen.coroutine
    def backup_image_coroutine(self):
        result = self.backup_image()
        raise gen.Return(result)

    @gen.coroutine
    def dump_image_coroutine(self):
        result = self.dump_image()
        raise gen.Return(result)

    def load_image(self):
        result = False
        try:
            LOG.info("loading image ...")
            image_path = os.path.join(CONFIG["data_path"], "auth_image")
            image = AppendLogJson(image_path)
            for line in image.iterlines():
                if line[I.cmd] == C.create_user:
                    self.create_user(
                        line[I.info]["name"],
                        line[I.info]["password"],
                        email = line[I.info]["email"],
                        phone = line[I.info]["phone"],
                        uid = line[I.info]["id"],
                        ctime = line[I.info]["ctime"],
                        mtime = line[I.info]["mtime"],
                        recover = True)
                elif line[I.cmd] == C.create_group:
                    self.create_group(
                        line[I.info]["name"],
                        line[I.info]["owner"],
                        users = line[I.info]["users"],
                        gid = line[I.info]["id"],
                        ctime = line[I.info]["ctime"],
                        mtime = line[I.info]["mtime"])
            result = True
        except Exception as e:
            LOG.exception(e)
        return result

    def load_editlog(self):
        result = False
        try:
            LOG.info("loading editlog ...")
            editlog_path = os.path.join(CONFIG["data_path"], "auth_editlog")
            editlog = AppendLogJson(editlog_path)
            for line in editlog.iterlines():
                if line[I.cmd] == C.create_user:
                    self.create_user(
                        line[I.info]["name"],
                        line[I.info]["password"],
                        email = line[I.info]["email"],
                        phone = line[I.info]["phone"],
                        uid = line[I.info]["id"],
                        ctime = line[I.info]["ctime"],
                        mtime = line[I.info]["mtime"],
                        recover = True)
                elif line[I.cmd] == C.create_group:
                    self.create_group(
                        line[I.info]["name"],
                        line[I.info]["owner"],
                        users = line[I.info]["users"],
                        gid = line[I.info]["id"],
                        ctime = line[I.info]["ctime"],
                        mtime = line[I.info]["mtime"])
                elif line[I.cmd] == C.update_user:
                    self.update_user(line[I.uid], data = line[I.data], recover = True)
                elif line[I.cmd] == C.update_group:
                    self.update_group(line[I.gid], data = line[I.data])
                elif line[I.cmd] == C.delete_user:
                    self.delete_user(line[I.uid])
                elif line[I.cmd] == C.delete_group:
                    self.delete_group(line[I.gid])
                elif line[I.cmd] == C.add_group_user:
                    self.add_group_user(line[I.gid], line[I.uid])
                elif line[I.cmd] == C.remove_group_user:
                    self.remove_group_user(line[I.gid], line[I.uid])
            result = True
        except Exception as e:
            LOG.exception(e)
        return result

    def backup_image(self):
        result = False
        try:
            LOG.info("backup image ...")
            now = datetime.datetime.now()
            now_suffix = now.strftime("%Y%m%d-%H%M%S")
            backup_image_path = os.path.join(CONFIG["data_path"], "auth_image.%s" % now_suffix)
            image_path = os.path.join(CONFIG["data_path"], "auth_image")
            backup_editlog_path = os.path.join(CONFIG["data_path"], "auth_editlog.%s" % now_suffix)
            editlog_path = os.path.join(CONFIG["data_path"], "auth_editlog")
            if os.path.exists(image_path) and not os.path.exists(backup_image_path):
                shutil.copy2(image_path, backup_image_path)
            if os.path.exists(editlog_path) and not os.path.exists(backup_editlog_path):
                shutil.copy2(editlog_path, backup_editlog_path)
            result = True
        except Exception as e:
            LOG.exception(e)
        return result

    def dump_image(self):
        result = False
        try:
            LOG.info("dumping image ...")
            new_image_path = os.path.join(CONFIG["data_path"], "auth_image.new")
            image_path = os.path.join(CONFIG["data_path"], "auth_image")
            old_image_path = os.path.join(CONFIG["data_path"], "auth_image.old")
            editlog_path = os.path.join(CONFIG["data_path"], "auth_editlog")
            LOG.debug("new image: %s", new_image_path)
            self.new_image = AppendLogJson(new_image_path)
            self.dump_users_groups()
            if os.path.exists(old_image_path):
                os.remove(old_image_path)
            if os.path.exists(image_path):
                os.rename(image_path, old_image_path)
            if os.path.exists(new_image_path):
                os.rename(new_image_path, image_path)
            if os.path.exists(editlog_path):
                os.remove(editlog_path)
            result = True
        except Exception as e:
            LOG.exception(e)
        return result

    def dump_users_groups(self):
        for uid in self.users:
            user = self.users[uid]
            if user["name"] != "unknown":
                LOG.debug("dump user[%s]: %s", uid, user)
                self.new_image.writeline({I.cmd: C.create_user, I.info: user})
        for gid in self.groups:
            group = self.groups[gid]
            if group["name"] != "everyone":
                LOG.debug("dump group[%s]: %s", gid, group)
                self.new_image.writeline({I.cmd: C.create_group, I.info: group})

    def close(self):
        pass
