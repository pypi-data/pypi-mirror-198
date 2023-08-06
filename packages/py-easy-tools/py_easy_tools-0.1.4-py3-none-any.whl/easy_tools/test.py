#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : pu mingzheng <pumz_1991@126.com>
# @Time     : 2023/03/20 16:01:13
# @File     : easy_tools - test.py
# @Software : python3.11 PyCharm
# @Desc     : TODO

import hmac
import math
import struct
import time
from abc import ABC, abstractmethod


class OTP:
    codeLength = 8
    timeSec = 30
    digest = "SHA1"

    @classmethod
    def get_code(cls, secret, time_slice=None):
        if time_slice is None:
            time_slice = math.floor(time.time() - OTP.timeSec)
            # 进行加密
        hm = hmac.new(key=secret.encode("utf-8"), msg=str(time_slice).encode("utf-8"), digestmod=OTP.digest).digest()
        # 进行二进制解包
        pack_array = struct.unpack(">L", hm[0:4])
        num = pack_array[0]
        # 补位
        num = num & 0x7FFFFFFF
        modulo = pow(10, OTP.codeLength)
        s_sum = str(num % modulo)
        s_sum = s_sum.zfill(OTP.codeLength)
        print(s_sum)
        return s_sum


class Main:
    def main(self):
        # secret由Eskyfun提供
        secret = "745a950f994b7da417cd438e5619ac7329400460"

        # 平台SDK提供token、userId参数
        token = "03c7c0ace395d80182db07ae2c30f034.1499671547.55935154"
        userId = "1000001"

        # 分割token
        tokenArray = token.split(".")
        if len(tokenArray) == 3:
            # 计数器
            times = tokenArray[1]
            # 验证码
            code = tokenArray[2]
            # 使用密钥和用户ID，拼接用户唯一密钥值
            userSecret = tokenArray[0] + userId + secret
            # 获取code
            oneCode = OTP.get_code(userSecret, times)
            # 对比验证
            if oneCode == code:
                # 成功
                print(1)
            else:
                # 失败
                print(0)
        else:
            # 失败
            print(0)


class A(ABC):
    def func(self):
        print(1)

    @abstractmethod
    def _func(self):
        print(1111111)


class B(A):
    def _func(self):
        print("B")
