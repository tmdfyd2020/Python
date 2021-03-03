################################
## 탭을 4개의 공백으로 바꾸기 ##
################################

# Question
# 문서 파일을 읽어서 그 문서 파일 안에 있는 tap을 공백 4개로 바꾸어 주는 스크립트를 작성해 보자.
# python tabto4.py a.txt b.txt 명령어로 a를 읽어서 tap을 공백으로 바꾸고 b에 쓰는 것이다.

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()
space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close() 
