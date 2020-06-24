print("this is test")
a = 4
if a>3:
    print("success")

for b in range(5):
    print("Shit")
#주석달기
for y in range(10):
    for x in range(y):
        print('*', end = '')
    print()

value = 1234
print(value)
print(value * 2)
a = 12
b = 34
print(a, b ,sep = ',')
print(a, b ,sep = '')
print(a, b ,sep = '--->')

s = '서울'
d = '대전'
g = '대구'
b = '부산'
print(s,d,g,b, sep = ' 찍고 ')

age = input('몇 살이세요?')
print(age)

price = input('가격을 입력하세요 : ')
num = input('개수를 입력하세요 : ')
sum = int(price) * int(num)
print('총액은', sum, '원입니다')