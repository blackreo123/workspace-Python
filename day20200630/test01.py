info_str = "20200630Rainy"

print("년도: ", info_str[:4])
print("월: ", info_str[4:6])
print("일: ", info_str[6:8])
print("날씨: ", info_str[8:])

abc_str = "abcdefghijk"

print(abc_str[2:7:2])
print(abc_str[::3])
print(len(abc_str))

str1 = "Java is fun! Python is fun, too!"

print(str1.find("Java"))
print(str1.rfind("fun"))
print(str1.find("PHP")) #없으면 -1 반환

print(str1.index("Python"))
print(str1.rindex("!"))
# print(str1.index("C#")) #error 발생!

num_list = ["3", "3.14","⅓"]


for num in num_list:
    print(num, ".isnumeric()=>", num.isnumeric())
    print(num, ".isdigit()=>", num.isdigit())
    print(num, ".isdecimal()=>", num.isdecimal())
    print()

str2 = str1.replace("fun","not fun")
print(str2)

str_list = str2.split("is")
print(str_list)

new_str = "**".join(str_list)
print(new_str)