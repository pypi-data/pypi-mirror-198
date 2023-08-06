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


class UsersHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        LOG.info("current_user: %s", self.current_user)
        if self.current_user.decode("utf-8") == "admin":
            self.render(
                "users/users.html",
                current_nav = "users",
                manager_host = "%s:%s" % (
                    self.get_name_http_host(),
                    CONFIG["name_http_port"]),
                user = self.current_user
            )
        else:
            result = {"result": Errors.OK}
            Errors.set_result_error("PermissionDenied", result)
            self.write(result)
            self.finish()

    @tornado.web.authenticated
    @gen.coroutine
    def put(self):
        result = {"result": Errors.OK}
        try:
            self.json_data = json.loads(self.request.body.decode("utf-8"))
            uid = self.get_json_argument("id", "")
            name = self.get_json_argument("name", "")
            password = self.get_json_argument("password", "")
            email = self.get_json_argument("email", "")
            phone = self.get_json_argument("phone", "")
            current_uid = self.get_user_uid().decode("utf-8")
            if current_uid == "admin" or current_uid == uid:
                client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"], token = self.get_user_token())
                success = client.update_user(uid, name = name, password = password, email = email, phone = phone)
                if not success:
                    Errors.set_result_error("OperationFailed", result)
            else:
                Errors.set_result_error("PermissionDenied", result)
        except OperationFailedError as e:
            Errors.set_result_error("OperationFailed", result, message = e.message.split(":")[-1])
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class UserHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        result = {"result": Errors.OK}
        try:
            offset = int(self.get_argument("offset", "0"))
            limit = int(self.get_argument("offset", "0"))
            current_uid = self.get_user_uid().decode("utf-8")
            client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"], token = self.get_user_token())
            r = client.list_users()
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
