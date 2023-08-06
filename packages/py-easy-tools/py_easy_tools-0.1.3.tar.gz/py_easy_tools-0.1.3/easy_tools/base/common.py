#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : pu mingzheng <pumz_1991@126.com>
# @Time     : 2023/03/14 10:48:38
# @File     : easy_tools/base - common.py
# @Software : python3.11 PyCharm
# @Desc     : TODO

import random
import re
import secrets

RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def get_random_string(length: int, allowed_chars: str = RANDOM_STRING_CHARS) -> str:
    """
    Return a securely generated random string.
    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)
    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    return "".join(secrets.choice(allowed_chars) for i in range(length))


def filter_special_character(string: str) -> str:
    """
    过滤参数
    字符 Unicode 编码范围
    数字: \u0030-\u0039
    汉字: \u4e00-\u9fa5
    大写字母: \u0041-\u005a
    小写字母: \u0061-\u007a
    :param string:
    :return:
    """
    return re.sub("([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", string)


def random_str(string: str) -> str:
    """
    打乱字符串
    :param string:
    :return:
    """
    string_list = list(string)
    random.shuffle(string_list)
    return "".join(string_list)


if __name__ == "__main__":
    a = "@#$#@%$%(*)*_(&*(^KGJHasd"
    print(filter_special_character(a))
    print(random_str(a))
