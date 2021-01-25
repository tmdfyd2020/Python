## 피보나치 함수 ##
# 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.
# 0, 1, 1, 2, 3, 5, 8, 13
# 입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.

## 내가 구현한 코드 ##

def Fibonacci(n):
    num = [0, 1]
    i = 2
    while True:
        if n == 0:
            print("1 이상의 수를 입력해주세요. ")
            break
        last = num[i-1] + num[i-2]  # num[i] == last 구하기
        if last > n:  # 구한 마지막 인수가 n을 넘으면 n을 넘기 직전까지의 i를 구해서 해당 i까지의 리스트를 출력한다.
            break
        num.extend([last])  # ☆ 리스트 확장에서 확장 인수를 리스트 형태로 넣어줘야 되는데 그냥 정수 형태로 넣어서 불가능! ☆
        i = i + 1
    return num

max = input("보고 싶은 피보나치 행렬의 최댓값을 입력하세요.")
print(Fibonacci(int(max)))

## 교재 코드 ##

def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))
