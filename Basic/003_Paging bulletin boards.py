#######################
## 게시판 페이징하기 ##
#######################

# Question
# A 씨는 게시판 프로그램을 작성하고 있다. 게시물의 총 건수와 한 페이지에 보여 줄 게시물의 수를 입력으로 주었을 때
# 총 페이지 수를 출력하는 프로그램이 필요하다고 한다.

def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
