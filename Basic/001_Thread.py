####################################
## 스레드를 다루는 threading 모듈 ##
####################################

import time  # sleep 함수를 쓰기 위한 모듈
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def long_task(): # 5초의 시간이 걸리는 함수
    for i in range(5):  # 1부터 5까지
        time.sleep(1)  # 1초간 대기한다.
        print("working : %s\n" % (i+1))

print("Start")

threads = []
for i in range(5):  # long_task를 5회 수행한다.
    t = threading.Thread(target=long_task)  # 스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start()  # 스레드를 실행한다.
    
for t in threads:
    t.join()  # join으로 스레드가 종료될 때까지 기다린다.

print("End") 
