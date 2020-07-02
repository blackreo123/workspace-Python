stocks = {"계란":500, "아이스크림":100, "라면":200}
keys = stocks.keys()
values = stocks.values()
items = stocks.items()

print(keys, type(keys))
print(values, type(values))
print(items, type(items))

for key in keys:
    print("품목명:",key, "/ 재고량:",stocks.get(key))

for item in items:
    print("품목명:", item[0], "/ 재고량:", item[1])

n=0
for value in values:
    n += 1
print(n)