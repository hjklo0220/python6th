# 함수
def pw(x, y):
	z = x ** y
	print(z)


pw(2, 5)


# pw(5, 2, 3) 파라미터 하나 더 받으면 오류

def show(name, age=30):
	print(f"name: {name}, Age: {age}")


show(age=90, name="test")
show(name="hello")

# 리스트
