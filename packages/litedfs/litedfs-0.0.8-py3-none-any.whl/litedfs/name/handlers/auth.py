# -*- coding: utf-8 -*-

import os
import json
import time
import random
import urllib
import logging
from uuid import uuid4

from tornado import web
from tornado import gen

from litedfs.name.handlers.base import BaseHandler, BaseSocketHandler
from litedfs.name.utils.auth_core import AuthSystem
from litedfs.name.utils.common import Errors
from litedfs.name.utils.common import InvalidValueError, SameNameExistsError, UserNotExistsError
from litedfs.name.utils.common import GroupNotExistsError, RecoverFailedError
from litedfs.name.config import CONFIG

LOG = logging.getLogger("__name__")


class UserHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                auth = AuthSystem.instance()
                result["data"] = auth.list_users()
            else:
                Errors.set_result_error("PermissionDenied", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @gen.coroutine
    def post(self):
        result = {"result": Errors.OK}
        try:
            self.json_data = json.loads(self.request.body.decode("utf-8"))
            name = self.get_json_argument("name", "")
            password = self.get_json_argument("password", "")
            email = self.get_json_argument("email", "")
            phone = self.get_json_argument("phone", "")
            if name and password:
                auth = AuthSystem.instance()
                success = auth.create_user(name, password, email = email, phone = phone)
                if not success:
                    Errors.set_result_error("OperationFailed", result)
            else:
                Errors.set_result_error("InvalidParameters", result)
        except SameNameExistsError:
            Errors.set_result_error("SameNameExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class UserUpdateDeleteHandler(BaseHandler):
    @gen.coroutine
    def get(self, uid):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                auth = AuthSystem.instance()
                result["data"] = auth.info_user(uid)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except UserNotExistsError:
            Errors.set_result_error("UserNotExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @gen.coroutine
    def put(self, uid):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                self.json_data = json.loads(self.request.body.decode("utf-8"))
                name = self.get_json_argument("name", "")
                password = self.get_json_argument("password", "")
                email = self.get_json_argument("email", None)
                phone = self.get_json_argument("phone", None)
                data = {}
                if name:
                    data["name"] = name
                if password:
                    data["password"] = password
                if email is not None:
                    data["email"] = email
                if phone is not None:
                    data["phone"] = phone
                if uid and data:
                    auth = AuthSystem.instance()
                    if self.current_user["id"] == uid or auth.is_admin(self.current_user["id"]):
                        success = auth.update_user(uid, data = data)
                        if not success:
                            Errors.set_result_error("OperationFailed", result)
                    else:
                        Errors.set_result_error("PermissionDenied", result)
                else:
                    Errors.set_result_error("InvalidParameters", result)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except UserNotExistsError:
            Errors.set_result_error("UserNotExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @gen.coroutine
    def delete(self, uid):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                if uid:
                    auth = AuthSystem.instance()
                    if self.current_user["id"] == uid or auth.is_admin(self.current_user["id"]):
                        success = auth.delete_user(uid)
                        if not success:
                            Errors.set_result_error("OperationFailed", result)
                    else:
                        Errors.set_result_error("PermissionDenied", result)
                else:
                    Errors.set_result_error("InvalidParameters", result)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class VerifyUserHandler(BaseHandler):
    @gen.coroutine
    def post(self):
        result = {"result": Errors.OK}
        try:
            self.json_data = json.loads(self.request.body.decode("utf-8"))
            name = self.get_json_argument("name", "")
            password = self.get_json_argument("password", "")
            if name and password:
                auth = AuthSystem.instance()
                valid = auth.is_valid_user(name, password)
                if not valid:
                    Errors.set_result_error("InvalidNameOrPassword", result)
            else:
                Errors.set_result_error("InvalidParameters", result)
        except UserNotExistsError:
            Errors.set_result_error("UserNotExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class GroupHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                auth = AuthSystem.instance()
                result["data"] = auth.list_groups()
            else:
                Errors.set_result_error("PermissionDenied", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @gen.coroutine
    def post(self):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                self.json_data = json.loads(self.request.body.decode("utf-8"))
                name = self.get_json_argument("name", "")
                owner = self.get_json_argument("owner", "")
                if name and owner:
                    auth = AuthSystem.instance()
                    success = auth.create_group(name, owner)
                    if not success:
                        Errors.set_result_error("OperationFailed", result)
                else:
                    Errors.set_result_error("InvalidParameters", result)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except UserNotExistsError:
            Errors.set_result_error("UserNotExists", result)
        except SameNameExistsError:
            Errors.set_result_error("SameNameExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class GroupUpdateDeleteHandler(BaseHandler):
    @gen.coroutine
    def get(self, gid):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                auth = AuthSystem.instance()
                result["data"] = auth.info_group(gid)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except GroupNotExistsError:
            Errors.set_result_error("GroupNotExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @gen.coroutine
    def put(self, gid):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                self.json_data = json.loads(self.request.body.decode("utf-8"))
                name = self.get_json_argument("name", "")
                owner = self.get_json_argument("owner", "")
                data = {}
                if name:
                    data["name"] = name
                if owner:
                    data["owner"] = owner
                if gid and data:
                    auth = AuthSystem.instance()
                    if auth.is_group_owner(gid, self.current_user["id"]) or auth.is_admin(self.current_user["id"]):
                        success = auth.update_group(gid, data = data)
                        if not success:
                            Errors.set_result_error("OperationFailed", result)
                    else:
                        Errors.set_result_error("PermissionDenied", result)
                else:
                    Errors.set_result_error("InvalidParameters", result)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except SameNameExistsError:
            Errors.set_result_error("SameNameExists", result)
        except UserNotExistsError:
            Errors.set_result_error("UserNotExists", result)
        except GroupNotExistsError:
            Errors.set_result_error("GroupNotExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @gen.coroutine
    def delete(self, gid):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                if gid:
                    auth = AuthSystem.instance()
                    if auth.is_group_owner(gid, self.current_user["id"]) or auth.is_admin(self.current_user["id"]):
                        success = auth.delete_group(gid)
                        if not success:
                            Errors.set_result_error("OperationFailed", result)
                    else:
                        Errors.set_result_error("PermissionDenied", result)
                else:
                    Errors.set_result_error("InvalidParameters", result)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class GroupUserHandler(BaseHandler):
    @gen.coroutine
    def put(self, gid, uid):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                if gid and uid:
                    auth = AuthSystem.instance()
                    if auth.is_group_owner(gid, self.current_user["id"]) or auth.is_admin(self.current_user["id"]):
                        success = auth.add_group_user(gid, uid)
                        if not success:
                            Errors.set_result_error("OperationFailed", result)
                    else:
                        Errors.set_result_error("PermissionDenied", result)
                else:
                    Errors.set_result_error("InvalidParameters", result)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except UserNotExistsError:
            Errors.set_result_error("UserNotExists", result)
        except GroupNotExistsError:
            Errors.set_result_error("GroupNotExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @gen.coroutine
    def delete(self, gid, uid):
        result = {"result": Errors.OK}
        try:
            if self.current_user:
                if gid and uid:
                    auth = AuthSystem.instance()
                    if auth.is_group_owner(gid, self.current_user["id"]) or auth.is_admin(self.current_user["id"]):
                        success = auth.remove_group_user(gid, uid)
                        if not success:
                            Errors.set_result_error("OperationFailed", result)
                    else:
                        Errors.set_result_error("PermissionDenied", result)
                else:
                    Errors.set_result_error("InvalidParameters", result)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class GenerateAuthTokenHandler(BaseHandler):
    @gen.coroutine
    def post(self):
        result = {"result": Errors.OK}
        try:
            self.json_data = json.loads(self.request.body.decode("utf-8"))
            name = self.get_json_argument("name", "")
            password = self.get_json_argument("password", "")
            expiration = self.get_json_argument("expiration", 3600)
            auth = AuthSystem.instance()
            user = auth.is_valid_user(name, password)
            if user:
                result["data"] = {}
                result["data"]["uid"] = user["id"]
                result["data"]["token"] = auth.generate_user_token(user["id"], expiration = expiration)
            else:
                Errors.set_result_error("InvalidNameOrPassword", result)
        except UserNotExistsError:
            Errors.set_result_error("UserNotExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class VerifyAuthTokenHandler(BaseHandler):
    @gen.coroutine
    def get(self, token):
        result = {"result": Errors.OK}
        try:
            auth = AuthSystem.instance()
            success = auth.verify_user_token(token)
            if not success:
                Errors.set_result_error("InvalidToken", result)
        except UserNotExistsError:
            Errors.set_result_error("UserNotExists", result)
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class LoginHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        result = {"result": Errors.OK}
        try:
            pass
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class LogoutHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        result = {"result": Errors.OK}
        try:
            pass
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()
