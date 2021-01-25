## 사칙연산 계산기 ##

class Calculator:
    def __init__(self, list):  # 생산자 : 객체를 생성하고 나서 별도의 함수를 입력하지 않고 생성과 동시에 기능을 수행
        self.list = list
    def sum(self):
        sum = 0
        for i in self.list:
            sum += i
        return sum

    def avg(self):
        total = self.sum()  # ☆
        return total / len(self.list)

cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())
