# 사전 생성
d = {}
print(type(d))
d[0] = "Hello"
print(d)
d["1"] = "World"
print(d)
d[0] = "Hi"
print(d)
del d[0]
print(d)
d.pop("1")
print(d)
# print(d[10])

d = {"a": 3.14, "b": 2.14, "c": 1.14}
d2 = {"a": 6.28, "b": 4.28, "c": 2.28, "d": 0.28}
d.update(d2)
print(d)