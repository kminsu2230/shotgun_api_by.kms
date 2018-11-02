#-*- coding : utf-8 -*-

import sys, os

# 샷건에 생성된 모든 프로젝트 검색
def project_all_search(sg):
    project_key = sg.find('Project',[])

    return project_key


# 샷건에 생성된 한가지의 프로젝트 검색
def project_search(sg,project):
    project_filter = [
        ['name','is',project]
    ]
    project_key = sg.find_one('Project',project_filter)
    if not project_key:
        return 
    
    return project_key 
