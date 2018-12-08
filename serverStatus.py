#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-11-28 11:32
# @Author  : Yangzan
# @File    : serverStatus.py

#!/usr/bin/python
#coding:utf-8


from subprocess import Popen,PIPE
import re
import os,sys
import paramiko


class GetLinuxMessage:
    #登录远程Linux系统
    def session(self, host, port, username, password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, int(port), username, password)
            print("Login %s is successful" % host)
            return ssh
        except Exception as e:
            print(e)
    #获取Linux主机名
    def get_hostname(self, host, port=22, username="root", password="baicells"):
        cmd_hostname = "hostname"
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command(cmd_hostname)
        hostname = stdout.read()
        return hostname

    #获取Linux网络ipv4信息
    def get_ifconfig(self, host, port=22, username="root", password="baicells"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("ifconfig")
        data = stdout.read()
        #ret = re.compile('((?:1[0-9][0-9]\.)|(?:25[0-5]\.)|(?:2[0-4][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))')
        ret = re.compile('(?:19[0-9]\.)((?:1[0-9][0-9]\.)|(?:25[0-5]\.)|(?:2[0-4][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){2}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))')
        match = ret.search(data).group()
        return match

    #获取Linux系统版本信息
    def get_version(self, host, port=22, username="root", password="baicells"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /etc/redhat-release")
        data = stdout.read()
        return data

    #获取Linux系统CPU信息
    def get_cpu(self, host, port=22, username="root", password="baicells"):
        cpunum = 0
        processor = 0
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/cpuinfo")
        cpuinfo = stdout.readlines()
        #with stdout.read() as cpuinfo:
        for i in cpuinfo:
            if i.startswith('physical id'):
                cpunum = i.split(":")[1]
            if i.startswith('processor'):
                processor = processor + 1
            if i.startswith('model name'):
                cpumode = i.split(":")[1]
        return int(cpunum)+1, processor,cpumode

    #获取Linux系统memory信息
    def get_memory(self, host, port=22, username="root", password="baicells"):

        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
        meminfo = stdout.readlines()
        #with open('/proc/meminfo') as meminfo:
        for i in meminfo:
            if i.startswith('MemTotal'):
                memory = int(i.split()[1].strip())
                memory = '%.f' %(memory / 1024.0) + 'MB'
            else:
                pass
        return memory

    #获取Linux系统网卡信息
    def get_ethernet(self, host, port=22, username="root", password="baicells"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("lspci")
        data = stdout.read()
        ret = re.compile('Eth[^\d].*')
        eth = ret.search(data).group()
        return eth


if __name__ == '__main__':
    host = input("please input the hostname: ")
    result = GetLinuxMessage()
    result1 = result.get_hostname(host)
    print ('主机名：%s' %result1)
    result2 = result.get_ifconfig(host)
    print ('主机IP：%s' %result2)
    result3 = result.get_version(host)
    print ('版本信息：%s' %result3)
    result4,result5,result6 = result.get_cpu(host)
    print ('物理CPU数量：%s' %result4)
    print ('逻辑CPU数量：%s' %result5)
    print ('物理CPU型号：%s' %result6)
    result7 = result.get_memory(host)
    print ('物理内存：%s' %result7)
    result8 = result.get_ethernet(host)
    print ('网卡型号：%s' %result8)