
# if
x = 5
if x > 3:
	print("x는 3보다 큼")

age = 18
if age >= 18:
	print("성인")
else:
	print("미성년자")

score = 50
if score >= 90:
	print("A")
else:
	if score >= 80:
		print("B")
	else:
		if score >= 70:
			print("C")
		else:
			print("D")

marks = 75
if marks >= 90:
	print("A")
elif marks >= 80:
	print("B")
elif marks >= 70:
	print("C")
else:
	print("D")

a = int(input("Enter number Greater then 2 : "))
if a >= 2:
	print("Correct! you have entered: ", a)
else:
	print("Wrong! you have entered: ", a)

day = input('요일을 입력: ')
if day == "Mon":
	print("월요일")
elif day == "Tue":
	print("화요일")
elif day == "Wed":
	print("수요일")
else:
	print("휴일")








