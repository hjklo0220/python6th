# 함수
# def pw(x, y):
# 	z = x ** y
# 	print(z)
#
#
# pw(2, 5)
#
#
# # pw(5, 2, 3) 파라미터 하나 더 받으면 오류
#
# def show(name, age=30):
# 	print(f"name: {name}, Age: {age}")
#
#
# show(age=90, name="test")
# show(name="hello")

# # Example1
# def add(x, y):
# 	z = x + y
# 	print("add: ", z)
#
#
# add(5, 2)
#
#
# # Example2
# def add(*num):
# 	z = num[0] + num[1] + num[2]
# 	print("add*: ", z)
#
#
# add(5, 2, 4)
#
#
# # Example3
# def add(x, *num):
# 	z = x + num[0] + num[1]
# 	print("add x*: ", z)
#
#
# add(5, 2, 4)

# # 가변 매개변수 (**)
# def add(x, **num):
# 	z = x + num['a'] + num['b'] + num['c']
# 	print("add: ", z)
#
#
# add(3, a=5, b=2, c=4, d=5)


# # 전역변수
# a = 50
#
#
# def show():
# 	x = 10
# 	print("x: ", x)  # local
# 	print("a: ", a)  # global
#
#
# show()
#
# print("Grobal Variable a: ", a)
# i = 0
#
#
# def myfunc():
# 	a = i + 1
# 	print("my func a: ", a)
#
#
# myfunc()
# print("Grobal Variable a:", a)


# i = 0
#
# def myfunc():
# 	i = i+1		# UnboundLocalError: local variable 'i' referenced before assignment
# 	print("my func i: ", i)
#
# myfunc()


# a = 50
# def show():
# 	a = 10
# 	print("show a: ", a)
#
# show()
# print("a: ", a)
#
# def show2():
# 	global a		# 명확하게 글로벌 변수 지정
# 	print('show2 a:', a)
# 	a = 20
# 	print('show2 a2: ',a)
#
# show2()
# print("a: ", a)		# 함수가 끝나도 값변경 그대로 적용


# 리스트
#
# fruits = ['apple', 'banana', 'cherry', 'ornage']
# print(fruits)
# fruits.append("grape")
# print(fruits)
# fruits.insert(2, "kiwi")
# print(fruits.pop())
# print(fruits)
# print("cherry index: ", fruits.index("cherry"))
# fruits.remove("cherry")  # 동일한 값이면 첫번째것만 지워짐
# print(fruits)
# fruits.reverse()
# print(fruits)


# fruits = ['apple', 'banana', 'cherry', 'ornage']
# vegetables = ["carrot", "cucumber"]
#
# grocery = fruits + vegetables
# print(grocery)
#
# numbers = [10, 5, 8, 1, 7]
# numbers.sort()  # 오름차순 정렬
# print(numbers)
#
# slice_numbers = numbers[1:4]
# print(slice_numbers)
#
# alias_numbers = numbers		# 이렇게 변수에 넣어서 쓰는것은 복사가 아님, 값 바뀌면 실제 numbers도 변경됨
# print(alias_numbers)
#
# copy_numbers = numbers.copy()
# print(copy_numbers)
#
# clone_numbers = numbers[:]
# print(clone_numbers)


# # 사용자 입력으로 리스트
# user_input_list = []
# num_elements = int(input("Enter number of element:"))
# for i in range(num_elements):
# 	user_input_list.append(input("Enter element:"))
#
# print("user input list:", user_input_list)


# 제네레이터

# def fibonacci(n):
# 	a, b = 0, 1
# 	for _ in range(n):
# 		yield a
# 		a, b = b, a + b
#
#
# runner = fibonacci(10)
#
# print(runner)
# print(next(runner))
#
# for num in runner:
# 	print(num)


# def generate_alpha(start_letter, end_letter):
# 	start = ord(start_letter)
# 	end = ord(end_letter)
# 	while start <= end:
# 		yield chr(start)
# 		start += 1
#
#
# runner = generate_alpha('A', 'F')
#
# print(type(runner))
# for letter in runner:
# 	print(letter)


# # 튜플
#
# b = (10)  # 값이 하나면 int로 되버림
# c = (10,)
# print(b, type(b))
# print(c, type(c))
#
# d = (10, 20, 30, 40)
# e = (10, 20, -50, 3.14, "hello")
# f = 10, 20, -50, 3.14, "hello"  # 괄호 생략 가능
#
# print(d, type(d))
# print(e, type(e))
# print(f, type(f))
#
# print(f[:3])  # 슬라이스 가능
# print(f[1:4])
#
# print(c + d)
# print(d * 3)
# print(-10 in f)
#
# h = (10, 20, 50, -60, 10, 30, 10)
# print(min(h), max(h))
# print(h.count(10))
# print(h.index(10))
# sorted_a = sorted(h)
# print(sorted_a)
#
# a = (10, 20, -50)
# x, y, z = a  # 언패킹, 갯수 일치하면 꺼낼수 있음
# print(x, y, z)
#
# a = 1
# b = 2
#
# a, b = b, a
#
# print(a, b)
#
# print(list(h), type(list(h)))
#
# nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# print(nested_tuple)


# # set
#
# a = {10, 20, 30}
# a = {10, 20, 30, "hello", 'set', 40}
#
# print(a)  # 중복된 값은 삭제되고 순서없음
# b = set()  # {}이렇게 선언하면 딕셔너리 먼저 찾기 때문에 set함수 써서 생성해야함
# print(b, type(b))
#
# # print(a[0])  # 인덱스 사용 못함(순서 없음)
# a.add(50)
# print(a)
# a.update([1, 2, 3, 4])
# print(a)
# a.remove("hello")  # remove는 요소 못찾으면 에러를 냄
# print(a)
# a.discard("hello") # 있으면 지워주고 없으면 지나감 에러없음, 더많이씀
# print(a)
#
# new_set = a.copy()
# print(new_set)
# new_set.clear()
# print(new_set)
#
#
# # 교집합
# b = {10, 20, 30, 'a', 'b', 'c'}
# intersection_a_b = a.intersection(b)
# print(intersection_a_b)
#
# # 합집합
# union_a_b = a.union(b)
# print(union_a_b)
#
# # 차집합
# difference_a_b = a.difference(b)
# print(difference_a_b)
#
# #부분집합
# c = {1, 2, 3}
# print(c.issubset(a))  # 지정된 셋(a)에 (c)의 값이 모두 포함되어 있으면 true
# print(a.issuperset(c))  # (a)안에 c가 모두 포함되어 있으면 True
#
# # 교집합을 뺀 나머지
# sym_a_b = a.symmetric_difference(b)
# print(sym_a_b)


# # dictionary
#
# stu = {101: 'A', 102: 'B', 103: 'C'}
# fees = {'A': 2000, 'B': 3000, 'C': 4000}
#
# print(stu[101])
# print(stu[102])
# print(stu[103])
#
# print(fees['A'])
# print(fees['B'])
# print(fees['C'])
#
# stu[102] = 'Python'  # 값 변경 가능
# print(stu)
#
# stu[104] = 'D'  # 값 추가
# print(stu)
#
# del stu[102]  # 값 제거
# print(stu)
#
# print(102 in stu)  # in, not in연산자 가능
# print(102 not in stu)
#
# # stu.clear()  # 전부 제거
# # print(stu)
#
# # new_stu = stu.copy()  # 복사
#
# key = (101, 102, 103)  # 키를 튜플로
# value = "test"
# new_stu = dict.fromkeys(key, value)
# print(new_stu)
#
# print(stu[101])
# print(stu.get(101))  # 위와 똑같
#
# print(stu.items(), type(stu.items()))
# print(stu.keys(), type(stu.keys()))
# print(stu.values())
# stu.update({105: "test"})
# print(stu)
# stu.pop(104)  # 키값으로 지울 수 있음
# print(stu)
# print(stu.pop(104, 'No value')) # 값이 없을때를 위해 디폴트 줄수 있음
#
# # set default
# stu.setdefault(104, 'apple')  # 값이 없을때만 그 값을 지정해 줌
# print(stu)
#
# print(stu.popitem())  # 순서는 없지만 추가한 넣은 순서대로 pop
# print(stu.popitem())
# print(stu.popitem())


# # call by reference, 참조를 이용한 함수 호출
# def val(lst):
# 	print("Inside Function Before append: ", lst, id(lst))
# 	lst.append(4)
# 	print("Inside Function After append: ", lst, id(lst))
#
# list = [1, 2, 3]
# print("Before Calling Function: ", list, id(list))
# val(list)
# print("After Calling Function: ", list, id(list))  # append한 그대로임
#
# print("==========")
# # call by value,
# def val(x):
# 	print("inside : ", x, id(x))
# 	x += 1
# 	print("inside add: ", x, id(x))
#
# a = 10
# print("befaoce calling: ", a, id(a))
# val(a)
# print("after calling", a, id(a))


# # 재귀
# import sys
# print("default: ", sys.getrecursionlimit())
# sys.setrecursionlimit(3000)
# i = 0
# def myfunc():
# 	global i
# 	i += 1
# 	print("myfunc: ", i)
# 	myfunc()
#
# myfunc()

# # 익명 함수
# show = lambda x: print(x)
#
# show(5)
#
# add = lambda x, y: (x + y)
#
# print(add(5, 2))
#
# add_sub = lambda x, y: (x + y, x - y)
# a, s = add_sub(5, 2)
#
# print(a)
# print(s)
#
# add = lambda x, y=3: (x + y)
# print(add(5))


# # 데코레이트
# def decor(func):
# 	def inner():
# 		a = func()
# 		add = a + 5
# 		return add
# 	return inner
#
# def num():
# 	return 10
#
# result_func = decor(num)
#
# print(result_func())
#
#
# @decor
# def num():
# 	return 10
#
#
# print(num())



from array import *

def show(ar):
	print("passed array ar: ", ar)
	print(type(ar))
	for i in ar:
		print(i)
	return ar


print()
a = array('i', [101, 102, 103, 104])
y = show(a)
print("return array Y :", y)
print(type(y))
for i in y:
	print(i)