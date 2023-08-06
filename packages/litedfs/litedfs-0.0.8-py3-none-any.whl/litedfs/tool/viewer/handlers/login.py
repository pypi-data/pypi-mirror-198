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


class LoginHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        self.render("login/login.html")

    @gen.coroutine
    def post(self):
        result = {"result": Errors.OK}
        try:
            self.json_data = json.loads(self.request.body.decode("utf-8"))
            name = self.get_json_argument("name", "")
            password = self.get_json_argument("password", "")
            email = self.get_json_argument("email", "")
            phone = self.get_json_argument("phone", "")
            login = self.get_json_argument("login", True)
            LOG.debug("login: %s, name: %s, password: %s, email: %s, phone: %s", login, name, password, email, phone)
            client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"])
            if login:
                r = client.generate_auth_token(
                        name,
                        password,
                        expiration = CONFIG["cookie_max_age_days"] * 24 * 3600
                )
                if r:
                    uid = r["data"]["uid"]
                    token = r["data"]["token"]
                    self.set_secure_cookie("name", name)
                    self.set_secure_cookie("password", password)
                    self.set_secure_cookie("uid", uid)
                    self.set_secure_cookie("token", token)
                else:
                    Errors.set_result_error("InvalidNameOrPassword", result)
            else:
                success = client.create_user(name, password, email = email, phone = phone)
                if not success:
                    Errors.set_result_error("OperationFailed", result)
        except OperationFailedError as e:
            Errors.set_result_error("OperationFailed", result, message = e.message.split(":")[-1])
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()


class LogoutHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        self.clear_cookie("name")
        self.clear_cookie("password")
        self.clear_cookie("token")
        self.redirect("/login")


class DeleteUserHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        uid = self.get_user_uid()
        client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"])
        success = client.delete_user(uid)
        if success:
            self.clear_cookie("name")
            self.clear_cookie("password")
            self.clear_cookie("token")
            self.redirect("/login")


class SettingsHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        result = {"result": Errors.OK}
        try:
            uid = self.get_user_uid()
            client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"])
            r = client.info_user(uid)
            if r:
                result["data"] = r["data"]
            else:
                Errors.set_result_error("OperationFailed", result)
        except OperationFailedError as e:
            Errors.set_result_error("OperationFailed", result, message = e.message.split(":")[-1])
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @tornado.web.authenticated
    @gen.coroutine
    def put(self):
        result = {"result": Errors.OK}
        try:
            self.json_data = json.loads(self.request.body.decode("utf-8"))
            name = self.get_json_argument("name", "")
            password = self.get_json_argument("password", "")
            email = self.get_json_argument("email", None)
            phone = self.get_json_argument("phone", None)
            uid = self.get_user_uid()
            user_name = self.current_user
            user_password = self.get_user_password()
            client = LiteDFSClient(self.get_name_http_host(), CONFIG["name_http_port"])
            success = client.update_user(uid, name = name, password = password, email = email, phone = phone)
            if success:
                if user_name != name or password != user_password:
                    r = client.generate_auth_token(
                            name,
                            password,
                            expiration = CONFIG["cookie_max_age_days"] * 24 * 3600
                    )
                    if r:
                        uid = r["data"]["uid"]
                        token = r["data"]["token"]
                        self.set_secure_cookie("name", name)
                        self.set_secure_cookie("password", password)
                        self.set_secure_cookie("uid", uid)
                        self.set_secure_cookie("token", token)
                    else:
                        Errors.set_result_error("InvalidNameOrPassword", result)
            else:
                Errors.set_result_error("OperationFailed", result)
        except OperationFailedError as e:
            Errors.set_result_error("OperationFailed", result, message = e.message.split(":")[-1])
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

