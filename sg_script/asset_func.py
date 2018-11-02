#-*- coding : utf-8 -*-
  
import sys, os

# 생성된 모든 어셋 검색 (쓸일은 없지만 예시로 적어둠)
def all_asset_list(sg):
    asset_list = sg.find("Asset",[])
    return asset_list

# 프로젝트명으로 어셋을 검색
def project_asset_list(sg,project_key):
    asset_filter = [['project','is',project_key]]
    asset_list = sg.find("Asset", asset_filter)
    return asset_list

# 어셋 이름으로 검색
def find_asset_name(sg, asset_name):
    # 마찬가지로 필드의 엔티티를 알고 있다면 'code' 가 아닌 다른걸 넣어서 사용 해도되며, 다른 엔티티를 추가로 넣어서 다중 필터로 사용해도 된다.
    asset_filter = [['code','is',asset_name]]
    asset_key = sg.find_one("Asset", asset_filter)
    return asset_key    
