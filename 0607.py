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
# 	print("A")
# else:
# 	if score >= 80:
# 		print("B")
# 	else:
# 		if score >= 70:
# 			print("C")
# 		else:
# 			print("D")
#
# marks = 75
# if marks >= 90:
# 	print("A")
# elif marks >= 80:
# 	print("B")
# elif marks >= 70:
# 	print("C")
# else:
# 	print("D")

# a = int(input("Enter number Greater then 2 : "))
# if a >= 2:
# 	print("Correct! you have entered: ", a)
# else:
# 	print("Wrong! you have entered: ", a)
#
# day = input('요일을 입력: ')
# if day == "Mon":
# 	print("월요일")
# elif day == "Tue":
# 	print("화요일")
# elif day == "Wed":
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
# while True:
# 	a = input("Enter Menu Number: ")
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
# while True:
# 	print("test")
# 	i += 1
# 	if i == 5:
# 		break	# 무한루프 탈출
# print("코드종료")
#
# i = 1
# while i <= 3:
# 	print("outer Loop", i)
# 	i += 1
# 	j = 1
# 	while j <= 5:
# 		print("Inner Loop", j)
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
# print("Reverse Rage with start, stop, step")
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
# 	pass  # FIXME test
# else:
# 	print("6보다 큼")	# TODO 작업 진행


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
# print("Array insert")
# stu_roll.insert(1, 106)
# stu_roll.insert(3, 107)
# n = len(stu_roll)
# i = 0
# while i < n:
# 	print(stu_roll[i])
# 	i += 1
#
# print("Array remove")
# stu_roll.remove(101)
# n = len(stu_roll)
# i = 0
# while i < n:
# 	print(stu_roll[i])
# 	i += 1
#
# print("Array pop")
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


print("array slicing")
print(stu_roll)
print("인덱스 1~4 까지")
print(stu_roll[1:5])
print("0~끝까지")
print(stu_roll[0:])
print("처음부터 5번째까지")
print(stu_roll[:5])
print("마지막 요소 4개")
print(stu_roll[-4:])
print("0부터 6번째 까지 2개씩 건너뛰어")
print(stu_roll[0:7:2])
print("마지막 5개 요소중 [-5 - (-3)] = -2 오른쪽으로부터 2개 요소 출력")
print(stu_roll[-5:-3])















