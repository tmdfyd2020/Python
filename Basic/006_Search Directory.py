#########################
## 하위 디렉터리 검색하기 ##
#########################

# Question
# 특정 디렉터리부터 시작해서 그 하위 모든 파일 중 파이썬 파일만 출력해주는 프로그램을 만들어보자.

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)  # listdir : 해당 디렉터리에 있는 파일들의 리스트를 구한다.
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)  # os.path.join : 디렉터리를 포함한 전체 경로를 구한다.
            if os.path.isdir(full_filename):  # full_filename이 디렉터리인지 파일인지 구별하기 위함  if 디렉터리 이면
                search(full_filename)  # 해당 디렉터리 파일이 디렉터리일 경우 다시 search 함수 호출(재귀호출) -> 모든 파일 검색
            else: # if 파일 이면
                # os.path.splitext : 파일 이름을 확장자를 기준으로 두 부분으로 나누어 준다.
                ext = os.path.splitext(full_filename)[-1]  # 해당 파일의 확장자 이름
                if ext == '.py':
                    print(full_filename)
    except PermissionError:  # os.listdir를 수행할 때 권한이 없는 디렉터리에 접근하더라도 프로그램이 오류로 종류하지 않고 수행
        pass

search("C:/")
