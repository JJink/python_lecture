#두개의 instance (first, second)
#다섯개의 method
class FourCal :
    def __init__(self, first, second) :
        self.first = first
        self.second = second
    def add(self) :
        return self.first + self.second
    def minus(self) :
        return self.first - self.second
    def mul(self) :
        return self.first * self.second
    def div(self) :
        return self.first / self.second


x = float(input("첫번째 숫자 : "))
y = float(input("두번째 숫자 : "))
a = FourCal(x,y)


print("두 수의 합 {}" .format(a.add()))
print("두 수의 차이 {}" .format(a.minus()))
print("두 수의 곱 {}" .format(a.mul()))
print("두 수의 몫 {}" .format(a.div()))

