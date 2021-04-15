data = 10
while data < 20 :
    print(data)
    data += 1

data = [1,2,3,4,5]
for i in data :
    print(i)

# welcome = 'welcome'
welcome = ['w','e','l','c','o','m','e']
for i in welcome :
    print('welcome to everyone!', i)


a = [1,2,3,4,5]

for i in a :
    print(i)
    print(i * 3)

st = 'Programing'
for ch in st :
    if ch in ['a','e','i','o','u']:
        break
    print(ch)
print('The End')

st = 'Programing'
for ch in st :
    if ch in ['a','e','i','o','u']:
        continue
    print(ch)
print('The End')

