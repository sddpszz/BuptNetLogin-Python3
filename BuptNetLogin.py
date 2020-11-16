# coding:utf-8
# ========== BuptNetLogin-Python3 [version 1.0.201116] =================
# Copyright (C) 2020 sddpszz@163.com
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =======================================================================
# 2020/11/16 python 3.7.9 32 bit 测试通过
# =======================================================================

import requests
import logging

logging.basicConfig(
    format="%(levelname)-8s %(asctime)s (%(filename)-15s: line %(lineno)3d): %(message)s",
    level=logging.INFO
)

Getway_IP = "http://10.3.8.211/login" # 校园网网关 ip 地址 或换成"http://gw.bupt.edu.cn/login"
Check_URL = "http://www.baidu.com"    # 用以检测是否可以连接到外网
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
username = "2020000000"               # 请改成自己的学工号
password = "********"                 # 请改成自己的校园网密码


def main():
    if check_network():
        logging.info("您已经登录过！")
        return True  # 已经登录
    else:
        login(username, password)
        if check_network():
            logging.info("登录成功！")
            return True  # 登录成功
        else:
            logging.error("登录失败，请检查账号密码！")
            return False  # 登录失败


def check_network():
    # 必须禁止重定向，否则 status_code 一直是 200
    res = requests.get(Check_URL, timeout=1, allow_redirects=False)
    logging.debug(res.status_code)
    logging.debug(res.text)
    if res.status_code == 200:
        logging.debug('您已经成功登录。')
        return True
    else:
        logging.debug('未登录。')
        return False


def login(username, password):
    params = {
        'user': username,
        'pass': password
    }
    res = requests.post(Getway_IP, headers=headers, params=params)
    logging.debug(res.text)
    return(res)

main()
