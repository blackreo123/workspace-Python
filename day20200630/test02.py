#형식문자
nums= 10 
days = "three"
s = "I ate %d apples, So I was sick %s days." % (nums, days)
print(s)

s2 = "I ate {apple} apples, So I was sick {sick} days.".format(apple=nums, sick=days) #{}안에 숫자 생략하면 알아서 차례대로 들어간다. , 변수명 지정해서도 가능
print(s2)