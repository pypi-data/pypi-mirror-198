#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : pu mingzheng <pumz_1991@126.com>
# @Time     : 2023/03/14 11:22:30
# @File     : easy_tools/base/encryption - rsa.py
# @Software : python3.11 PyCharm
# @Desc     : TODO
import base64
import hashlib
import uuid
from typing import Tuple

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature


def generator_rsa(key_length_in_bits: int = 1024, filename: str = "") -> Tuple[bytes, bytes]:
    """
    生成 rsa 秘钥
    :param key_length_in_bits: Select the length of your key pair between 512 and 16384 bits
    :param filename:
    :param save:
    :return:
    """
    random_generator = Random.new().read
    rsa = RSA.generate(key_length_in_bits, random_generator)
    rsa_private_key = rsa.exportKey()
    rsa_public_key = rsa.publickey().exportKey()

    if filename:
        with open(f"{filename}_private.pem", "w") as f:
            f.write(rsa_private_key.decode())
        with open(f"{filename}_public.pem", "w") as f:
            f.write(rsa_public_key.decode())
    print(len(rsa_private_key))  # 866
    print(len(rsa_public_key))  # 271
    return rsa_private_key, rsa_public_key


def get_key(str_key):
    key = RSA.importKey(str_key)
    return key


# 公钥加密
def rsa_public_encode(password, public_key):
    cipher = PKCS1_cipher.new(RSA.importKey(public_key))
    encrypt_text = base64.b64encode(cipher.encrypt(password.encode("utf-8")))
    return encrypt_text.decode("utf-8")


# 私钥解密
def rsa_private_decode(password, private_key):
    cipher = PKCS1_cipher.new(RSA.importKey(private_key))
    decrypt_text = cipher.decrypt(base64.b64decode(password), Random.new().read)
    return decrypt_text.decode("utf-8")


# 私钥签名
def rsa_private_sign(data, private_key):
    private_key = RSA.importKey(private_key)
    signer = PKCS1_signature.new(private_key)
    digest = SHA256.new()
    digest.update(data.encode("utf8"))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    signature = signature.decode("utf-8")
    return signature


# 公钥验证
def rsa_public_sign(text, sign, public_key):
    public_key = RSA.importKey(public_key)
    verifier = PKCS1_signature.new(public_key)
    digest = SHA256.new()
    digest.update(text.encode("utf-8"))
    return verifier.verify(digest, base64.b64decode(sign))


# 设置 MD5 为文件名
def filename2md5(filename):
    md5 = hashlib.md5()
    md5.update(filename.encode())
    return md5.hexdigest().upper()


# 设置 uuid 为文件名
def filename2uuid(filename):
    return uuid.uuid4().hex.upper()


if __name__ == "__main__":
    generator_rsa(filename="soul")
