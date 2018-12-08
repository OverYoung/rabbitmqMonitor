#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-11-26 10:07
# @Author  : Yangzan
# @File    : getData.py

import os
import subprocess
import json
import requests
import time

def getData():
    #调用API获取rabbitmq状态数据
    r = requests.get(url=('http://10.10.10.144:15672/api/nodes'), auth=('admin', 'admin@144'))
    data = json.loads(r.text[1:][:-1])

    FileDescriptions_used      = data['fd_used']
    FileDescriptions_limit     = data['fd_total']
    Socket_descriptors_used    = data['sockets_used']
    Socket_descriptors_limit   = data['sockets_total']
    Erlang_processes_used      = data['proc_used']
    Erlang_processes_limit     = data['proc_total']
    Memory_used                = data['mem_used']
    Memory_limit               = data['mem_limit']
    DiskSpace_free             = data['disk_free']
    DiskSpace_limit            = data['disk_free_limit']
    Uptime                     = data['uptime']

    message = "时间："+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())\
                      + "\n"\
              "内存占用为："+ str(Memory_used/1024/1024) + " MB" \
                                                    "\n" \
              "总内存为："+ str(Memory_limit/1024/1024/1024)+ " GB"
    return message