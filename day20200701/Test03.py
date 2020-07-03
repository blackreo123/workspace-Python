# 튜플 생성
t = tuple("python"); l = list("python")
# t[0] = "f" # 튜플은 immutable

# tuple unpacking
breakfast, lunch, dinner = \
("씨리얼", "오크우드호텔 식당", "피자")
print(breakfast)
print(lunch)
print(dinner)

# tuple unpacking 응용
a = 0
b = 10
temp = a
a = b
b = temp
print(a, b)

a, b = (0, 10)
a, b = b, a
print(a, b) # pythonic한 코드