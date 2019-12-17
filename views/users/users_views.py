# ! / usr / bin / python3
# -*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

from models.user import (
    Users
)

# 从commons中导入http_response方法
from common.commons import (
    http_response,
)

# 从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
)

########## Configure logging #############
logFilePath = "log/users/users.log"
logger = logging.getLogger("Users")
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(logFilePath, when="D", interval=1, backupCount=30)
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s', )
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)

class LoginHandle(tornado.web.RequestHandler):
   """handle /user/regist request
   :param phone: users sign up phone
   :param password: users sign up password
   """

   @property
   def db(self):
       return self.application.db

   def get(self):
       try:
           #获取入参
           phone = self.get_argument( "phone" )
           password = self.get_argument( "password" )
       except:
           #获取入参失败时，抛出错误码及错误信息
           logger.info("LoginHandle: request argument incorrect")
           http_response(self, ERROR_CODE['1001'], None, 1001)
           return

       #从数据库 Users 表查找入参中的 phone 是否存在
       ex_user = self.db.query(Users).filter_by(phone=phone).first()
       if ex_user:
           #如果手机号已存在，返回首页 H5 页面 index.html
           logger.debug( "LoginHandle: get user login: %s" %phone )
           self.render( "index.html", user=ex_user, title="用户页面" )
           self.db.close()
           return
       else:
           #用户不存在，提示用户未注册
           http_response( self, ERROR_CODE['1003'], None, 1003 )
           self.db.close()
           return



class RegistHandle(tornado.web.RequestHandler):
    """handle /user/regist request
    :param phone: users sign up phone
    :param password: users sign up password
    :param code: users sign up code, must six digital code
    """

    @property
    def db(self):
        return self.application.db

    def get(self):
        http_response(self, ERROR_CODE['0'], None, 0)

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['verify_code']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            logging.info("RegistHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], None, 1001)
            return

        ex_user = self.db.query(Users).filter_by(phone=phone).first()

        if ex_user:
            http_response(self, ERROR_CODE['1002'], None, 1002)
            self.db.close()
            return
        else:
            logger.debug("RegistHandle: insert db, user: %s" % phone)
            create_time = datetime.now()
            add_user = Users(phone, password, create_time)
            self.db.add(add_user)
            self.db.commit()
            self.db.close()
            # 处理成功后，返回成功码“0”及成功信息“ok”
            logger.debug("RegistHandle: regist successfully")
            http_response(self, ERROR_CODE['0'], None, 0)