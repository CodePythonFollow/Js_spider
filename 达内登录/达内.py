#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: 达内.py
@time: 2019/10/7 22:43
'''
import execjs
pass_word = input('请输如密码:')

js = open('tooc.js')

password = execjs.compile(js.read()).call('MD5', pass_word)

print(password)