#! /usr/bin/python3
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from .home_views import (
    HomeHandle,
)

urls = [
    # 从 / 过来的请求，将调用 home_views 里面的 HomeHandle 类
    (r'*', HomeHandle)
]
