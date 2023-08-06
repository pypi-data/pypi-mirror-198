# -*- coding: utf-8 -*-

import os
import json
import time
import shutil
import datetime
import logging

from tornado import web
from tornado import gen

from litedfs.name.utils.append_log import AppendLogJson
from litedfs.tool.editor.handlers.base import BaseHandler, BaseSocketHandler
from litedfs.tool.editor.utils.common import Errors
from litedfs.tool.editor.config import CONFIG

LOG = logging.getLogger("__name__")


class FileSystemHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        self.render(
            "filesystem/filesystem.html",
            current_nav = "filesystem"
        )


class FileSystemLogsHandler(BaseHandler):
    fsimage = AppendLogJson(os.path.join(CONFIG["data_path"], "fsimage"))
    editlog = AppendLogJson(os.path.join(CONFIG["data_path"], "editlog"))
    fsimage.indexlines()
    editlog.indexlines()
    actions = {
        "c": "create",
        "mds": "makedirs",
        "md": "makedir",
        "d": "delete",
        "r": "rename",
        "m": "move",
        "cp": "copy",
        "ur": "update_replica",
        "ufi": "update_file_info",
        "upd": "update_parent_dirs",
    }

    def readlines(self, start = 1):
        if start in FileSystemLogsHandler.fsimage.lines_pos:
            for line in FileSystemLogsHandler.fsimage.iterlines(start = start):
                yield line
            for line in FileSystemLogsHandler.editlog.iterlines(start = 1):
                yield line
        else:
            start = start - FileSystemLogsHandler.fsimage.lines()
            for line in FileSystemLogsHandler.editlog.iterlines(start = start):
                yield line

    @gen.coroutine
    def get(self):
        result = {"result": Errors.OK}
        try:
            offset = int(self.get_argument("offset", 0))
            limit = int(self.get_argument("limit", 0))

            delete_path = os.path.join(CONFIG["data_path"], "tmp", "delete")
            edit_path = os.path.join(CONFIG["data_path"], "tmp", "edit")

            fsimage_total = FileSystemLogsHandler.fsimage.lines()
            editlog_total = FileSystemLogsHandler.editlog.lines()
            total = fsimage_total + editlog_total
            result["offset"] = offset
            result["limit"] = limit
            result["fsimage_total"] = fsimage_total
            result["editlog_total"] = editlog_total
            result["total"] = total
            result["logs"] = []
            n = 0
            for line in self.readlines(start = offset):
                line_num = offset + n
                delete_file = os.path.join(delete_path, "%s" % line_num)
                edit_file = os.path.join(edit_path, "%s" % line_num)
                status = "normal"
                new = {}
                if os.path.exists(delete_file):
                    status = "delete"
                elif os.path.exists(edit_file):
                    status = "edit"
                    with open(edit_file, "r") as fp:
                        new = json.loads(fp.read())
                log = {
                    "num": line_num,
                    "action": FileSystemLogsHandler.actions[line["c"]],
                    "path": line["p"] if "p" in line else "",
                    "ctime": "",
                    "mtime": "",
                    "raw": line,
                    "status": status,
                    "new": new,
                    "source": ("E-%s" % (line_num - fsimage_total)) if line_num > fsimage_total else ("F-%s" % line_num),
                }
                if "i" in line:
                    if "ctime" in line["i"]:
                        log["ctime"] = datetime.datetime.fromtimestamp(line["i"]["ctime"]).strftime("%Y-%m-%d %H:%M:%S")
                    if "mtime" in line["i"]:
                        log["mtime"] = datetime.datetime.fromtimestamp(line["i"]["mtime"]).strftime("%Y-%m-%d %H:%M:%S")
                result["logs"].append(log)
                if n == limit - 1:
                    break
                n += 1
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()

    @gen.coroutine
    def put(self):
        result = {"result": Errors.OK}
        try:
            self.json_data = json.loads(self.request.body.decode("utf-8"))
            command = self.get_json_argument("command", "")
            params = self.get_json_argument("params", {})

            delete_path = os.path.join(CONFIG["data_path"], "tmp", "delete")
            edit_path = os.path.join(CONFIG["data_path"], "tmp", "edit")

            if command:
                LOG.info("command: %s, params: %s", command, params)
                if command == "clean_all":
                    if os.path.exists(delete_path):
                        shutil.rmtree(delete_path)
                        LOG.info("remove: %s", delete_path)
                        os.mkdir(delete_path)
                        LOG.info("mkdir: %s", delete_path)
                    if os.path.exists(edit_path):
                        shutil.rmtree(edit_path)
                        LOG.info("remove: %s", edit_path)
                        os.mkdir(edit_path)
                        LOG.info("mkdir: %s", edit_path)
                elif command == "delete" and params:
                    line_num = params["line_num"]
                    with open(os.path.join(delete_path, "%s" % line_num), "w") as fp:
                        fp.write("%s" % line_num)
                elif command == "delete_cancel":
                    line_num = params["line_num"]
                    file_path = os.path.join(delete_path, "%s" % line_num)
                    if os.path.exists(file_path) and os.path.isfile(file_path):
                        os.remove(file_path)
                elif command == "edit":
                    line_num = params["line_num"]
                    content = params["content"]
                    with open(os.path.join(edit_path, "%s" % line_num), "w") as fp:
                        fp.write(json.dumps(content))
                elif command == "edit_cancel":
                    line_num = params["line_num"]
                    file_path = os.path.join(edit_path, "%s" % line_num)
                    if os.path.exists(file_path) and os.path.isfile(file_path):
                        os.remove(file_path)
                elif command == "export":
                    export_fsimage_path = os.path.join(CONFIG["data_path"], "tmp", "export", "fsimage")
                    export_editlog_path = os.path.join(CONFIG["data_path"], "tmp", "export", "editlog")
                    if os.path.exists(export_fsimage_path) and os.path.isfile(export_fsimage_path):
                        os.remove(export_fsimage_path)
                    if os.path.exists(export_editlog_path) and os.path.isfile(export_editlog_path):
                        os.remove(export_editlog_path)
                    fsimage = AppendLogJson(export_fsimage_path)
                    editlog = AppendLogJson(export_editlog_path)
                    fsimage_total = FileSystemLogsHandler.fsimage.lines()
                    editlog_total = FileSystemLogsHandler.editlog.lines()
                    n = 0
                    for line in self.readlines():
                        line_num = n + 1
                        delete_file = os.path.join(delete_path, "%s" % line_num)
                        edit_file = os.path.join(edit_path, "%s" % line_num)
                        status = "normal"
                        new = {}
                        if os.path.exists(delete_file):
                            status = "delete"
                        elif os.path.exists(edit_file):
                            status = "edit"
                            with open(edit_file, "r") as fp:
                                new = json.loads(fp.read())

                        if line_num > fsimage_total:
                            if status == "normal":
                                editlog.writeline(data = line)
                            elif status == "edit":
                                editlog.writeline(data = new)
                        else:
                            if status == "normal":
                                fsimage.writeline(data = line)
                            elif status == "edit":
                                fsimage.writeline(data = new)
                        n += 1
                else:
                    pass
        except Exception as e:
            LOG.exception(e)
            Errors.set_result_error("ServerException", result)
        self.write(result)
        self.finish()
