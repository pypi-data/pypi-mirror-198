#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : pu mingzheng <pumz_1991@126.com>
# @Time     : 2023/03/14 10:48:38
# @File     : easy_tools/base/encryption - translate.py
# @Software : python3.11 PyCharm
# @Desc     : TODO

from aes import AESHandler


# str translate demo
def str_translate(
    string: str = "",
    in_table: str = "123qwertyuiop456asdfghjkl789zxcvbnm ",
    out_table: str = "~!@#$%789^&*()_+-=654,.<>/;312:[]{}'",
    back: bool = False,
) -> str:
    if back:
        in_table, out_table = out_table, in_table

    translate_table = str.maketrans(in_table, out_table)

    return string.translate(translate_table)


def aes_str_translate(string: str, in_table: str, out_table: str, aes_key: str = "", back: bool = False) -> str:
    aes = AESHandler(aes_key)
    in_table = aes.decrypt_AES(in_table)
    out_table = aes.decrypt_AES(out_table)

    return str_translate(string, in_table, out_table, back)


def test_aes_str_translate(string: str, back: bool = False) -> str:
    default_in_table = "123qwertyuiop456asdfghjkl789zxcvbnm "
    default_out_table = "~!@#$%789^&*()_+-=654,.<>/;312:[]{}'"
    aes_key = "cfd71c5af6a9168d3c2d9aa5c21649fa"

    aes = AESHandler(aes_key=aes_key)
    in_table = aes.encrypt_AES(default_in_table)
    out_table = aes.encrypt_AES(default_out_table)

    return aes_str_translate(string, in_table, out_table, aes_key, back)


if __name__ == "__main__":
    pass
    # a = str_translate("show me the money")
    # b = str_translate(a, True)
    # print(a)
    # print(b)

    string = "show me the money"
    a = test_aes_str_translate(string)
    b = test_aes_str_translate(a, True)
    print(a)
    print(b)
