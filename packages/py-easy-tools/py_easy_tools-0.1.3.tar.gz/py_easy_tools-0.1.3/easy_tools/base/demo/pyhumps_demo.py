#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : pu mingzheng <pumz_1991@126.com>
# @Time     : 2023/03/14 11:43:46
# @File     : easy_tools/base/demo - pyhumps_demo.py
# @Software : python3.11 PyCharm
# @Desc     : TODO

import humps

humps.camelize("jack_in_the_box")  # jackInTheBox
humps.decamelize("rubyTuesdays")  # ruby_tuesdays
humps.pascalize("red_robin")  # RedRobin
humps.kebabize("white_castle")  # white-castle

array = [{"attrOne": "foo"}, {"attrOne": "bar"}]
humps.decamelize(array)  # [{"attr_one": "foo"}, {"attr_one": "bar"}]

array = [{"attr_one": "foo"}, {"attr_one": "bar"}]
humps.camelize(array)  # [{"attrOne": "foo"}, {"attrOne": "bar"}]

array = [{"attr_one": "foo"}, {"attr_one": "bar"}]
humps.kebabize(array)  # [{'attr-one': 'foo'}, {'attr-one': 'bar'}]

array = [{"attr_one": "foo"}, {"attr_one": "bar"}]
humps.pascalize(array)  # [{"AttrOne": "foo"}, {"AttrOne": "bar"}]

humps.is_camelcase("illWearYourGranddadsClothes")  # True
humps.is_pascalcase("ILookIncredible")  # True
humps.is_snakecase("im_in_this_big_ass_coat")  # True
humps.is_kebabcase("from-that-thrift-shop")  # True
humps.is_camelcase("down_the_road")  # False

humps.is_snakecase("imGonnaPopSomeTags")  # False
humps.is_kebabcase("only_got_twenty_dollars_in_my_pocket")  # False


# what about abbrevations, acronyms, and initialisms? No problem!
humps.decamelize("APIResponse")  # api_response


# # aws.py
# import humps
# import boto3
#
# def api(service, decamelize=True, *args, **kwargs):
#     service, func = service.split(":")
#     client = boto3.client(service)
#     kwargs = humps.pascalize(kwargs)
#     response = getattr(client, func)(*args, **kwargs)
#     return (depascalize(response) if decamelize else response)
#
# # usage
# api("s3:download_file", bucket="bucket", key="hello.png", filename="hello.png")
