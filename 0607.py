# # if
# x = 5
# if x > 3:
# 	print("x는 3보다 큼")
#
# age = 18
# if age >= 18:
# 	print("성인")
# else:
# 	print("미성년자")
#
# score = 50
# if score >= 90:
# 	print("a")
# else:
# 	if score >= 80:
# 		print("b")
# 	else:
# 		if score >= 70:
# 			print("c")
# 		else:
# 			print("d")
#
# marks = 75
# if marks >= 90:
# 	print("a")
# elif marks >= 80:
# 	print("b")
# elif marks >= 70:
# 	print("c")
# else:
# 	print("d")

# a = int(input("enter number greater then 2 : "))
# if a >= 2:
# 	print("correct! you have entered: ", a)
# else:
# 	print("wrong! you have entered: ", a)
#
# day = input('요일을 입력: ')
# if day == "mon":
# 	print("월요일")
# elif day == "tue":
# 	print("화요일")
# elif day == "wed":
# 	print("수요일")
# else:
# 	print("휴일")


# # 반복문
#
# i = 0
# while i < 10:
# 	i += 1
# 	print(i)
# else:
# 	print("else")  # while문에 else쓸 수 있음, while문이 끝나면 실행됨
#
# while true:
# 	a = input("enter menu number: ")
# 	if a == '0':
# 		break
# 	print("a: ", a)
# else:
# 	print("else")  # break로 나가면 else실행 안됨
#
# a = 1
# while a <= 5:
# 	print(a)
# 	a += 1
# print("코드 종료")
#
# a = 2
# while a <= 10:
# 	print(a)
# 	a += 2
# print("종료")
#
# a = 1
# while a <= 5:
# 	print(a)
# 	a += 1
# else:
# 	print("while 조건이 거짓이므로 else부분 실행됨")
# print("종료")
#
# # 무한 루프
# i = 0
# while true:
# 	print("test")
# 	i += 1
# 	if i == 5:
# 		break	# 무한루프 탈출
# print("코드종료")
#
# i = 1
# while i <= 3:
# 	print("outer loop", i)
# 	i += 1
# 	j = 1
# 	while j <= 5:
# 		print("inner loop", j)
# 		j += 1
# print("종료")


# # range함수
# for i in range(5):
# 	print(i)
#
# for i in range(2, 7):
# 	print(i)
#
# for i in range(1, 10, 2):
# 	print(i)
#
# for i in range(-1, -10, -2):
# 	print(i)
#
# print("reverse rage with start, stop, step")
# r = range(5, 0, -1)
# for i in r:
# 	print(i)


# # for loop
# st = "hello"
# for ch in st:
# 	print(ch)
# else:
# 	print("else")
# print("코드 종료")


# # pass
# a = 5
# if a < 6:
# 	pass  # fixme test
# else:
# 	print("6보다 큼")	# todo 작업 진행


# # 배열
# import array
# stu_roll = array.array('i', [101, 102, 103, 104, 105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])
#
# print("for in")
# for ele in stu_roll:
# 	print(ele)
#
# print("index를 이용")
# n = len(stu_roll)
# for i in range(n):
# 	print(i, "=", stu_roll[i])
#
# print("while")
# i = 0
# while i < n:
# 	print(i, "=", stu_roll[i])
# 	i += 1

# # 배열 추가 삭제
from array import *

stu_roll = array('i', [101, 102, 103, 104, 105, 106, 107])
# n = len(stu_roll)
# i = 0
# while i < n:
# 	print(stu_roll[i])
# 	i += 1
#
# print("array insert")
# stu_roll.insert(1, 106)
# stu_roll.insert(3, 107)
# n = len(stu_roll)
# i = 0
# while i < n:
# 	print(stu_roll[i])
# 	i += 1
#
# print("array remove")
# stu_roll.remove(101)
# n = len(stu_roll)
# i = 0
# while i < n:
# 	print(stu_roll[i])
# 	i += 1
#
# print("array pop")
# stu_roll.pop(2)
# n = len(stu_roll)
# i = 0
# while i < n:
# 	print(stu_roll[i])
# 	i += 1

# print("array index")
# print(stu_roll.index(103))
#
# print("array extend")
# arr = array('i', [201, 202, 203])
# stu_roll.extend(arr)
# n = len(stu_roll)
# i = 0
# while i < n:
# 	print(stu_roll[i])
# 	i += 1
#
# print("array reverse")
# stu_roll.reverse()
# n = len(stu_roll)
# i = 0
# while i < n:
# 	print(stu_roll[i])
# 	i += 1


# print("array slicing")
# print(stu_roll)
# print("인덱스 1~4 까지")
# print(stu_roll[1:5])
# print("0~끝까지")
# print(stu_roll[0:])
# print("처음부터 5번째까지")
# print(stu_roll[:5])
# print("마지막 요소 4개")
# print(stu_roll[-4:])
# print("0부터 6번째 까지 2개씩 건너뛰어")
# print(stu_roll[0:7:2])
# print("마지막 5개 요소중 [-5 - (-3)] = -2 오른쪽으로부터 2개 요소 출력")
# print(stu_roll[-5:-3])


# 문자열
str1 = "hello"
str2 = "python"
str3 = '''
	hi
		hello
			python
'''


# print(str1)
# print(str2)
# print(str3)
#
# str4 = "aaa'bb'aa"
# str5 = 'xxxx"aa"xxx'
# print(str4)
# print(str5)
#
# str6 = "hello \n bye"
# str7 = "hello \\n bye"
# str8 = r"hello \n bye"
#
# print(str6)
# print(str7)
# print(str8)

# # 문자열 함수
# s = "Hello world"
# print(s.upper())  # 모두대문자
# print(s.lower())  # 모두소문자
# print(s.swapcase())  # 대소문자 변경
# print(s.title())  # 맨 앞자만 대문자
# print(s.isupper())  # 모두 대문자면 True
# print(s.islower())  # 모두 소문자면 True
# print(s.istitle())  # 맨앞자 대문자면 True
#
# print(s.isdigit())  # 숫자면 True
# print(s.isalpha())  # 알파벳만 있으면 True
#
# print(s.lstrip())	# 왼쪽 공백 제거
# print(s.rstrip())	# 오른쪽 공백 제거
# print(s.strip())	# 양옆 공백 제거
#
# print(s.replace("world", "there"))	# 문자열 변경
# print(s.split(" "))	# 문자열 분리
# split = s.split(" ")
# print(" ".join(split))	# 문자열 합성
#
# print(s.startswith("Hello"))	# 해당문자열이 Hello로 시작하면 True
# print(s.endswith("ld"))	# 문자열이 ld로 끝나는


# 함수
# def disp():
# 	name = "phthon"
# 	print("hello", name)
#
#
# disp()
# disp()
# disp()
#
#
# def add(y):
# 	x = 10
# 	z = x + y
# 	print(z)
#
#
# add(20)
#
# def add(y):
# 	x = 10.1234
# 	print(x + y)
# 	print(f"Formatted Output:{x + y:6.2f}")	# ":" 명세 하는것 f:float 숫자는 6칸으로 소수2자리까지
#
# add(20)

# def add():
# 	x = 10
# 	y = 20
# 	z = x + y
# 	return z
#
#
# print(add())
#
#
# def add():
# 	x = 10
# 	y = 20
# 	return x + y
#
#
# print(add())
#
#
# def add(y):
# 	x = 10
# 	return x + y
#
#
# print(add(10))
#
# def add(y):
# 	x = 10
# 	c = x + y
# 	d = y - x
# 	return c, d, 50
#
#
# print(add(20), type(add(20)))

# 중첩 함수
def disp():
	def show():
		print("Show")	# 나중에 출력 (선언만 한거임)
		return "Show Function"
	result = show() + "disp Function"
	print("disp")		# 먼저 출력됨
	return result


print(disp())

def disp(sh):
	print(type(sh))
	print("disp function" + sh())	# 파라미터로 함수를 받을 수 있음


def show():
	return " show function"


disp(show)	# 함수 클래스

def disp():
	def show():
		return "show Function"

	print("disp Function")
	return show		# ()쓰면 실행되기 때문에 그냥 함수 리턴


r_sh = disp()
print(r_sh(), type(r_sh))
