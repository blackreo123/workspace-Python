l = [0,1,2]
print(l)

l.append(3)
print(l)

l.insert(2, 1.5)
print(l)

# l=list("python")
# print(l)

l=[0,1,2]
l[1]= [3,4,5]
print(l)

l=[0,1,2]
l[1:1] = [3,4,5]
print(l)

l.remove(3)
print(l)

del l[1]
print(l)

a = l.pop()#기본 맨뒤 숫자 넣으면 인덱스 
print(a)
print(l)