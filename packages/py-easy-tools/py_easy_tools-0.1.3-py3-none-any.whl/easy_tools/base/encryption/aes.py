#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : pu mingzheng <pumz_1991@126.com>
# @Time     : 2023/03/14 10:48:38
# @File     : easy_tools/base/encryption - aes.py
# @Software : python3.11 PyCharm
# @Desc     : TODO

import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESHandler:
    def __init__(self, aes_key: str):
        # self.aes_key = hashlib.md5(aes_key.encode("utf-8")).hexdigest().encode()
        self.aes_key = aes_key.encode()

    def signature(self):
        ...

    def encrypt_AES(self, data: str, block_size=32):
        raw = pad(data.encode(), block_size)
        cipher = AES.new(self.aes_key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw)).decode()

    def decrypt_AES(self, data: str, block_size=32):
        enc = base64.b64decode(data)
        cipher = AES.new(self.aes_key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc), block_size).decode()


if __name__ == "__main__":
    aes_key = "cfd71c5af6a9168d3c2d9aa5c21649fa"
    aes = AESHandler(aes_key)
    s = "123456"
    en_s = aes.encrypt_AES(s)
    de_s = aes.decrypt_AES(en_s)
    print(en_s, de_s)
