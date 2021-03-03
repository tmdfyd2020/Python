#########################
## 간단한 메모장 만들기 ##
#########################

# Question
# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.
# python memo.py -a "Life is too short" 와 같은 명령을 실행했을 때 메모를 추가하고,
# python memo.py -v 명령을 실행하면 메모가 출력되도록 만들어보자.

import sys

option = sys.argv[1]  # argv[0]은 파일 이름이다.

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()

elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo) 
