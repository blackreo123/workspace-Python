#자바스러운 코드
squares = list()
for i in range(1,11):
    squares.append(i**2)
print(squares)

#파이썬스러운 코드
squares2=[i**2 for i in range(1, 11)]
print(squares2)

#자바스러운 코드
combs = list()
for i in [1,2,3]:
    for j in [2,3,4]:
        if i==j:
            combs.append((i, j))
print(combs)

#파이썬스러운 코드
combs2 = [(i,j) for i in [1,2,3] for j in [2,3,4] if i==j]
print(combs2)

#파이썬스러운 코드
from math import pi
print([str(round(pi,i)) for i in range(1,6)])

#파이썬스러운 코드
vec = [[1,2,3], [4,5,6], [7,8,9]]
num_list = [num for elem in vec for num in elem]
print(num_list)

#comprehensionㅌ을 이용한 구구단 출력
gugudan = ["{} * {} = {}".format(i,j,i*j) for i in range(2,10) for j in range(1,10)]
for i in range(len(gugudan)):
    print(gugudan[i], end=" ")
    if (i+1) % 3 == 0:
        print()

prime_set = set(range(2,21))-{x for x in range(2,21) for y in range(2,x)if x% y ==0}
print(prime_set)