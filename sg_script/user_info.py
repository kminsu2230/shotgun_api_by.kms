#-*- coding : utf-8 -*-

import sys, os

# 샷건의 모든 유저
def get_user_list(sg):
    user_list = sg.find("HumanUser",[])
    return list

# 샷건의 유저 아이디를 알고 있으시 그 유저만 검색
def get_user_find(sg, user_id):
    user_key = sg.find_one("HumanUser",[['login','is',user_id]])
    return user_key
