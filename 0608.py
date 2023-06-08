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

def fibonacci(n):
	a, b = 0, 1
	for _ in range(n):
		yield a
		a, b = b, a + b


runner = fibonacci(10)

print(runner)
print(next(runner))

for num in runner:
	print(num)
