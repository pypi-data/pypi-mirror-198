# -*- coding: utf-8 -*-

import json
import time
import logging

from tornado import web
from tornado import gen

from litedfs.tool.editor.handlers.base import BaseHandler, BaseSocketHandler
from litedfs.tool.editor.config import CONFIG

LOG = logging.getLogger("__name__")


class EditLogHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        self.write("editlog handler")
        self.finish()
