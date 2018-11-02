#-*- coding : utf-8 -*-
  
import sys, os

# 생성된 모든 샷 검색 (쓸일은 없지만 예시로 적어둠)
def all_shot_list(sg):
    shot_list = sg.find("Shot",[])
    return shot_list

# 프로젝트명으로 샷을 검색
def project_shot_list(sg,project_key):
    shot_filter = [['project','is',project_key]]
    shot_list = sg.find("Shot", shot_filter)
    return shot_list

# 샷 이름으로 검색
def find_shot_name(sg, shot_name):
    # 마찬가지로 필드의 엔티티를 알고 있다면 'code' 가 아닌 다른걸 넣어서 사용 해도되며, 다른 엔티티
를 추가로 넣어서 다중 필터로 사용해도 된다.
    shot_filter = [['code','is',shot_name]]
    shot_key = sg.find_one("Shot", shot_filter)
    return shot_key
