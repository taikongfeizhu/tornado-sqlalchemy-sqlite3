#! /usr/bin/python3
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///./data.db?charset=utf8', encoding="utf8", echo=False)
BaseDB = declarative_base()

SERVER_HEADER = "http://127.0.0.1:8000"

ERROR_CODE = {
    "0": "success",
    #Users error code
    "1001": "入参非法",
    "1002": "用户已注册，请直接登录",
    "1003": "用户尚未注册，请先注册",
    "2001": "上传图片不能为空"
}