
# print("hello python")
# a="아나콘다"
# print(a)
# print(type(a))

# print(len(a)) #정수타입: 길이를 잴 수 없다.

# print(a.find('b')) # find() :리턴값 인덱스)

# #임의의 객체(아무 값이나)를 '순서대로' 지정하는 집합형태의 자료형
# #군집자료형 : 리스트,tuple,dict,set
# #list :값 변경가, []와 쉼표로 구분
# #tuple : 불가능
# #dict

# #print(id(a))# a의 주소값 출력
# #print(a.append(6)  #none , append()리턴값 없음 --->출력불가

# #함수
# #두개 이상의 값을 반환하면, 결과 값은 튜플로 반환
# #매개변수의 자료형은 동적으로 결정되며, 호출되는 순간 해당인자에 전달되는 개게에 따라 자료형이 결정됨

# a={'b':'Ace',1:[1,2,3],(1,2):'bb'}
# print(a[1])
# print(a['b'])
# print(a[(1,2)])
# print(type(a))
# print(a.keys())
# print(a.values())
# print(a.items())
# print(a)
# print(type(a))

# a= list(a) ##list 타입으로 형 변환
# a=set(a) #set 타입으로 형변환
# a= list(a)
# print("ahah")
# a.reverse()
# print(a)
# a=tuple(a)
# print(a)
# a= list(a)
# a.reverse()
# print(a)

# a="""안뇽핫에ㅕ
# 제이름은 잘부탁입니다.
# 아나"""

# print(a)

# a=5;
# a+=3
# print(divmod(5,3))
# print(pow(5,3))

# print(a.title())   # Abcd Abcd 단어별 첫 글짜 -> 대문자
# print(a.find('g')) #-1리턴 ( 없음 의미 )
# ########################################

# s=set[1,2,3]
# s.add(4)
# print(s)
# s.update([5])
# print(s)
# s.remove(5)
# print(s)
# s.update([6,7])
# s.update([3,]) # , 찍어서 튜플임 보여주기
# s.update(s)
# print(str,)
# #####조건문(if)#######################
# # 리턴값 : 불 자료형

##a=True
#False : 0이거나 없는수
##print(bool(3,))# Ture
#값이 있는 애는 true 로 출력됨
#a=1
#b=2

#a[[1,2,3]
# a.append(), a.remove(), a.sort(), a.reverse()


a=[1,2,3]
a.reverse()
print(a)
a=set(a)# 집합으로 변경
print(a)


##모듈사용 :파이썬의 크다란 특징

import collections.abc
obj=[1,2,3,4]
obj2={1,2,3,4}

print(isinstance(obj,collections.abc.Iterable))# True
print(isinstance(obj2,collections.abc.Iterable))# True
