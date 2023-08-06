# -*- coding: utf-8 -*-

import os
import logging
import argparse
from uuid import uuid4

from litedfs.version import __version__
from litedfs.name.utils.fs_core import F, C
from litedfs.name.utils.append_log import AppendLogJson
from litedfs.name.config import CONFIG, load_config
from litedfs.name import logger

LOG = logging.getLogger(__name__)


class DirectoryInfoNotExistsError(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = 'migrate_fsimage_generate_directory_ids.py')
    parser.add_argument("-c", "--config", required = True, help = "configuration file path")
    parser.add_argument("-v", "--version", action = 'version', version = '%(prog)s ' + __version__)
    args = parser.parse_args()
    if args.config:
        success = load_config(args.config)
        if success:
            logger.config_logging(file_name = "migrate_fsimage_generate_directory_ids.log",
                                  log_level = CONFIG["log_level"],
                                  dir_name = CONFIG["log_path"],
                                  day_rotate = False,
                                  when = "D",
                                  interval = 1,
                                  max_size = 20,
                                  backup_count = 5,
                                  console = True)

            LOG.info("migrate start")
            
            fsimage_new_path = os.path.join(CONFIG["data_path"], "fsimage.new")
            fsimage_path = os.path.join(CONFIG["data_path"], "fsimage")
            fsimage_bak_path = os.path.join(CONFIG["data_path"], "fsimage.bak")
            fsimage_new = AppendLogJson(fsimage_new_path)
            fsimage = AppendLogJson(fsimage_path)
            n = 1
            for line in fsimage.iterlines():
                if line[F.cmd] == C.makedir:
                    directory_id = str(uuid4())
                    if F.info in line:
                        line[F.info]["id"] = directory_id
                    else:
                        raise DirectoryInfoNotExistsError("line: %s: %s" % (n, line))
                fsimage_new.writeline(line)
                n += 1
            fsimage_new.close()
            fsimage.close()

            os.rename(fsimage_path, fsimage_bak_path)
            os.rename(fsimage_new_path, fsimage_path)

            LOG.info("migrate end")
        else:
            print("failed to load configuration: %s" % args.config)
    else:
        parser.print_help()