#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-12-08 18:49
# @Author  : Yangzan
# @File    : 1.py

import smtplib

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from_addr = 'yangzan@mail.bdsmc.net'
password = '7635313222Yz'  #填入授权码, 而不是邮箱登陆密码

to_addr = 'yangzan@mail.bdsmc.net'

smtp_server = 'smtp.ym.163.com' #使用QQ邮箱发送

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg = MIMEText('I am Neil Zeng, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....', 'utf-8').encode()

server = smtplib.SMTP()
server.set_debuglevel(1)
server.connect(smtp_server)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()