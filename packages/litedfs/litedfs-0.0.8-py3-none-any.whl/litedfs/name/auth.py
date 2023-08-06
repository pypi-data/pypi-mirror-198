#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import logging
import argparse

import tornado.ioloop

from litedfs.version import __version__
from litedfs.name.utils.auth_core import AuthSystem, UserNotExistsError
from litedfs.name.utils import common
from litedfs.name.config import CONFIG, load_config
from litedfs.name import logger

LOG = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(prog = 'ldfsauth')
    parser.add_argument("-u", "--uid", required = True, help = "user id", default = "")
    parser.add_argument("-n", "--name", help = "user name", default = None)
    parser.add_argument("-p", "--password", help = "user password", default = None)
    parser.add_argument("-e", "--email", help = "user email", default = None)
    parser.add_argument("-P", "--phone", help = "user phone number", default = None)
    parser.add_argument("-c", "--config", help = "run auth command with configuration file")
    parser.add_argument("-v", "--version", action = 'version', version = '%(prog)s ' + __version__)
    args = parser.parse_args()
    if args.config:
        success = load_config(args.config)
        if success:
            common.init_storage()
            logger.config_logging(file_name = "auth.log",
                                  log_level = CONFIG["log_level"],
                                  dir_name = CONFIG["log_path"],
                                  day_rotate = False,
                                  when = "D",
                                  interval = 1,
                                  max_size = 20,
                                  backup_count = 5,
                                  console = True)

            LOG.info("start")

            try:
                auth_system = AuthSystem()
                auth_system.recover()
                if args.uid == "admin":
                    try:
                        user = auth_system.info_user(args.uid)
                        data = {}
                        if args.name == "admin":
                            data["name"] = "admin"
                        if args.password is not None:
                            data["password"] = args.password
                        if args.email is not None:
                            data["email"] = args.email
                        if args.phone is not None:
                            data["phone"] = args.phone
                        if data:
                            success = auth_system.update_user(args.uid, data = data)
                            if success:
                                print("update admin successed")
                            else:
                                print("update admin failed")
                        else:
                            print(json.dumps(user, indent = 4))
                    except UserNotExistsError:
                        if args.password:
                            email = ""
                            if args.email is not None:
                                email = args.email
                            phone = ""
                            if args.phone is not None:
                                phone = args.phone
                            success = auth_system.create_user("admin", args.password, email = email, phone = args.phone, uid = "admin")
                            if success:
                                print("create admin successed")
                            else:
                                print("create admin failed")
                        else:
                            print("need name(\"admin\") & password to create admin")
                elif args.uid:
                    try:
                        user = auth_system.info_user(args.uid)
                        data = {}
                        if args.name is not None:
                            data["name"] = args.name
                        if args.password is not None:
                            data["password"] = args.password
                        if args.email is not None:
                            data["email"] = args.email
                        if args.phone is not None:
                            data["phone"] = args.phone
                        if data:
                            success = auth_system.update_user(args.uid, data = data)
                            if success:
                                print("update %s successed" % args.uid)
                            else:
                                print("update %s failed" % args.uid)
                        else:
                            print(json.dumps(user, indent = 4))
                    except UserNotExistsError:
                        if args.password and args.name:
                            email = ""
                            if args.email is not None:
                                email = args.email
                            phone = ""
                            if args.phone is not None:
                                phone = args.phone
                            success = auth_system.create_user(args.name, args.password, email = email, phone = args.phone)
                            if success:
                                print("create %s successed" % args.name)
                            else:
                                print("create %s failed" % args.name)
                        else:
                            print("need name & password to create user")
                else:
                    print("uid should be a string")
                auth_system
            except Exception as e:
                LOG.exception(e)

            LOG.info("end")
        else:
            print("failed to load configuration: %s" % args.config)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
