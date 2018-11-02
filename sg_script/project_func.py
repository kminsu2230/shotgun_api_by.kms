#-*- coding : utf-8 -*-

import sys, os
import shotgun_api3

# 개인이 작성한것이므로 사용하는곳에서 넣어서 사용하시면 됩니다.
studio_host = "https//domain.shotgunstudio.com"
script_name = "scprit_name"
script_key = "~~~~~~~~~~~~~~~~~~~"

sg = shotgun_api3.Shotgun(studio_host, script_name, script_key)

#---------------------------------------------------------------------------
'''
# 참고사항 1
find,find_one 명령어의 경우 (엔티티, 필터값, 보이게될 필드) 이렇게 구성되어 있다.
find : [{}] 배열상태로 있는 딕셔너리
find : {} 배열이없는 딕셔너리

# 참고사항 2
# class를 사용해 속성을 만들어서 추가하는게 효율이 좋다. (편의성) 
'''
#--------------------------------------------------------------------------




# 샷건에 생성된 모든 프로젝트 검색
def project_all_search(project):
    project_key = sg.find('Project',[])

    return project_key


# 샷건에 생성된 한가지의 프로젝트 검색
def project_search(project):
    project_filter = [
        ['name','is',project]
    ]
    project_key = sg.find_one('Project',project_filter)
    if not project_key:
        return 
    
    return project_key 
