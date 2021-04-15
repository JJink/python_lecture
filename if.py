age = 18
if age < 20 :
    print("청소년 할인")

walk = 1100
if walk >= 1000 :
    print("목표달성")

time = 14
if time < 12 :
    print("오전입니다.")
elif time >= 12 :      
    print("오후입니다.")


a = 10
b = 13

if (a % 2 == 0 and b % 2 == 0) :
    print("a,b 둘 다 짝수 입니다.")
elif (a % 2 == 0 or b % 2 ==0) :
    print("a,b 둘 중 하나만 짝수 입니다.")


pocket = ['paper', 'cellphone']
card = False
if 'money' in pocket :
    print("택시를 탄다")
elif card :
    print('택시를 탄다')
else :
    print('걸어간다')
