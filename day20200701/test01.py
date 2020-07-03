# 리스트 생성
l = list("python")
print(l)

l = [0, 1, 2]
print(l)

# 리스트 요소 추가
l.append(3)
print(l)

l.insert(2, 1.5)
print(l)

# 인덱싱과 슬라이싱으로 요소 변경or추가
l = [0, 1, 2]
l[1] = [3, 4, 5]
print(l)

l = [0, 1, 2]
l[1:1] = [3, 4, 5]
print(l)

# 리스트 요소 제거
l.remove(3)
print(l)

# 리스트에 있는 모든 요소 제거 -> 이런 경우 집합으로 형변환하고 처리하는 게 더 알맞음
l = [3, 3, 3, 3, 2, 1]
while True:
    if 3 in l:
        l.remove(3)
    else:
        break
print(l)

del l[1]
print(l)

a = l.pop(1)
print(a, l)