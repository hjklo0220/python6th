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


# range함수
for i in range(5):
	print(i)

for i in range(2, 7):
	print(i)

for i in range(1, 10, 2):
	print(i)

for i in range(-1, -10, -2):
	print(i)

print("Reverse Rage with start, stop, step")
r = range(5, 0, -1)
for i in r:
	print(i)






