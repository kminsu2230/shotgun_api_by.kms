#-*- coding : utf-8 -*-
  
import sys, os


# 프로젝트명으로 테스크을 검색
def project_task_list(sg,project_key):
    task_filter = [['project','is',project_key]]
    taskt_list = sg.find("Task", task_filter)
    return task_list

# 유저 정보를 가지고 테스크 검색
def find_task_name(sg, user_key):
    # 마찬가지로 필드의 엔티티를 알고 있다면 'user'  가 아닌 다른걸 넣어서 사용 해도되며, 다른 엔티티를 추가로 넣어서 다중 필터로 사용해도 된다.
    task_filter = [['task_assignees','is',user_key]]
    task_key = sg.find_one("Task", task_filter)
    return task_key
