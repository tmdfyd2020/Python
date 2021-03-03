## 평균값 구하기 ##
# 아래와 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후
# 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.
# 70 60 55 75 95 90 80 80 85 100

## 내 코드 ##

f = open("C:/python/sample.txt", 'r')
data = f.read()  # 한 줄씩 읽는다.
num = data.split("\n")  # \n을 기준으로 파일 내용을 구분하여 list에 저장한다.

sum = 0
for i in num:
    sum += int(i)
average = sum / len(list)

f = open("C:/python/result.txt", 'w')
f.write(str(average))
f.close()

## ☆ f.write로 들어가는 내용은 정수는 안되고 문자열만 가능하다! ☆ ##

## 교재 코드 ##

f = open("sample.txt")
lines = f.readlines()  # sample.txt를 줄 단위로 모두 읽는다.
f.close()

total = 0
for line in lines:
  score = int(line)
  total += score
 average = total / len(lines) 
