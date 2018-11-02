# shotgun_api_by.kms
    AutoDesk shotgun 홈페이지를 가면 알 수 있는 내용이나 영어로 되있기에 자주 사용할 것만모아서 적은  api 이다
#-*- coding : utf-8 -*-

# 개인이 작성한것이므로 사용하는곳에서 넣어서 사용하시면 됩니다.
 기본 베이스는 아래 sg가 작성되있는 기준으로 만들어 두었습니다. (파일마다 적으면 연결시간이 걸림으로..)
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


# code
     python2.7

# reference site
     http://developer.shotgunsoftware.com/python-api/reference
