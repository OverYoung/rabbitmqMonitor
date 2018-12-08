#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-11-26 10:07
# @Author  : Yangzan
# @File    : test.py

import os
import subprocess

server = '10.10.10.142'
tmpres = os.popen('curl -i -u admin:admin@142 http://10.10.10.142:15672/api/vhosts').readlines()
print(len(tmpres))
print(tmpres)

print("ok..")