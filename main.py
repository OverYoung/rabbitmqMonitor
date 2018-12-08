#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-12-08 18:01
# @Author  : Yangzan
# @File    : main.py
import getData
import mail
import log
import smtplib
import time

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from_addr = 'yangzan@mail.bdsmc.net'
password = '7635313222Yz'  #填入授权码, 而不是邮箱登陆密码

to_addr = '390091733@qq.com'

smtp_server = 'smtp.ym.163.com' #使用QQ邮箱发送

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
while True:
    now = time.localtime(time.time())
    if(now.tm_min == 15 and now.tm_sec >=58):
        msg = MIMEText(getData.getData(), 'plain', 'utf-8')
        msg['From'] = _format_addr('杨赞<%s>' % from_addr)
        #msg['To'] = _format_addr('monitor <%s>' % to_addr)
        msg['Subject'] = Header('144rabbitmq监控', 'utf-8').encode()

        server = smtplib.SMTP()
        #server.set_debuglevel(1)
        server.connect(smtp_server)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        #server.sendmail(from_addr, ['yangzan@mail.bdsmc.net'], msg.as_string())
        server.quit()
