# import random

# words=['cookie','apple','banana']

# print(words[int(random.random()*3)])
# words=['cookie','apple','banana','melon','blueberry']

# print(words[int(random.random()*5)])
# print(words[random.randint(0,4)])

# ##random.randit(시작,끝번호) 정수값의 범위를 랜덤하게 뽑아줌

# #중복제거: set()
# print(random.randint(1,45))
# lotto=[]

# while True:
#     lotto.append(random.randint(1,45))
#     lotto=list(set(lotto))
#     if len(lotto)==5:
#         break
# print(lotto)

# ##funtion that use in list[]
# # append(),reverse(),remove(),sort() ...
# ## way2 to remove dupulication

# lotto=[]
# while len(lotto) <5:
#     num = random.randint(1,45)
#     check=True
#     for i in lotto:
#         if i ==num:
#             check =False
#         if check:
#             lotto.append(num)
            
# print(lotto)


import turtle, random

def getrgb():
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)
 
t= turtle.Turtle() ##객체생성- > 생성자동작-> 객체의 참조를  t에 넣음

t.shape('turtle') ## 거북이 생성

r, g, b = getrgb()
 
for i in range(0,5):
    turtle.color('r', 'g','b')
    turtle.begin_fill()
    t.forward(100)
    t.left(144)
    
turtle.end_fill()

