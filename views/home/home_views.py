# ! / usr / bin / python3
# -*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler

# 从commons中导入http_response方法
from common.commons import (
    http_response,
)

# 从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
)

########## Configure logging #############
logFilePath = "log/home/home.log"
logger = logging.getLogger("Home")
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(logFilePath, when="D", interval=1, backupCount=30)
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s', )
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)

class HomeHandle(tornado.web.RequestHandler):
   """handle / request
   """

   @property
   def db(self):
       return self.application.db

   def get(self):
       logger.info("LoginHandle: request argument incorrect")
       data = "weclome to tornado"
       http_response(self, ERROR_CODE['0'], data, 0)
