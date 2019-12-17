#! /usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from .users_views import (
    RegistHandle,
    LoginHandle
)

urls = [
    # 从 /users/regist/ 过来的请求，将调用 users_views 里面的 RegistHandle 类
    (r'regist/', RegistHandle),
    # http://127.0.0.1:8000/users/login/?phone=1888888888&password=123457
    (r'login/', LoginHandle)
]
