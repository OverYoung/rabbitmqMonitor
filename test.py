#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-11-26 10:07
# @Author  : Yangzan
# @File    : test.py

import os
import subprocess

#访问服务器状态
server = '10.10.10.144'
tmpres = os.popen('curl -i -u admin:admin@144 http://10.10.10.144:15672/api/nodes').readlines()
print(len(tmpres))
for x in tmpres:
    print(x)