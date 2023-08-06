# -*- coding: utf-8 -*-

import json
import time
import logging

import tornado
from tornado import web
from tornado import gen
from litedfs_client.client import LiteDFSClient, OperationFailedError

from litedfs.tool.viewer.handlers.base import BaseHandler, BaseSocketHandler
from litedfs.tool.viewer.utils.common import Errors
from litedfs.tool.viewer.config import CONFIG

LOG = logging.getLogger("__name__")


class GroupsHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        self.render(
            "groups/groups.html",
            current_nav = "groups",
            manager_host = "%s:%s" % (
                self.get_name_http_host(),
                CONFIG["name_http_port"]),
            user = self.current_user
        )

    @tornado.web.authenticated
    @gen.coroutine
    def put(self):
        result = {"result": Errors.OK}
        try:
            self.json_data = json.loads(self.request.body.decode("utf-8"))
            gid = self.get_json_argument("id", "")
            name = self.get_json_argument("name", "")
            owner = self.get_json_argument("owner", "")
            current_uid = self.get_user_uid().decode("utf-8")
            client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"], token = self.get_user_token())
            success = client.update_group(gid, name = name, owner = owner)
            if not success:
                Errors.set_result_error("OperationFailed", result)
        except OperationFailedError as e:
            Errors.set_result_error("OperationFailed", result, message = e.message.split(":")[-1])
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class GroupHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        result = {"result": Errors.OK}
        try:
            offset = int(self.get_argument("offset", "0"))
            limit = int(self.get_argument("offset", "0"))
            current_uid = self.get_user_uid().decode("utf-8")
            client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"], token = self.get_user_token())
            r = client.list_groups()
            if r:
                result = r
            else:
                Errors.set_result_error("OperationFailed", result)
        except OperationFailedError as e:
            Errors.set_result_error("OperationFailed", result, message = e.message.split(":")[-1])
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class GroupUserHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def put(self, gid, uid):
        result = {"result": Errors.OK}
        try:
            current_uid = self.get_user_uid().decode("utf-8")
            if gid and uid:
                client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"], token = self.get_user_token())
                r = client.info_group(gid)
                if r:
                    if current_uid == "admin" or current_uid == r["data"]["owner"]:
                        success = client.add_group_user(gid, uid)
                        if not success:
                            Errors.set_result_error("OperationFailed", result)
                    else:
                        Errors.set_result_error("PermissionDenied", result)
            else:
                Errors.set_result_error("InvalidParameters", result)
        except OperationFailedError as e:
            Errors.set_result_error("OperationFailed", result, message = e.message.split(":")[-1])
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @tornado.web.authenticated
    @gen.coroutine
    def delete(self, gid, uid):
        result = {"result": Errors.OK}
        try:
            current_uid = self.get_user_uid().decode("utf-8")
            if gid and uid:
                client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"], token = self.get_user_token())
                r = client.info_group(gid)
                if r:
                    if current_uid == "admin" or current_uid == r["data"]["owner"]:
                        success = client.remove_group_user(gid, uid)
                        if not success:
                            Errors.set_result_error("OperationFailed", result)
                    else:
                        Errors.set_result_error("PermissionDenied", result)
            else:
                Errors.set_result_error("InvalidParameters", result)
        except OperationFailedError as e:
            Errors.set_result_error("OperationFailed", result, message = e.message.split(":")[-1])
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()
