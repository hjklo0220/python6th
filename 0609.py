# 클래스 네임스페이스, 인스턴스 네임스페이스 차이
class Moblie:
	fp = "yes"


realme = Moblie()  # 생성자 함수, 이 클래스를
redme = Moblie()
geek = Moblie()

print(Moblie.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)


Moblie.fp = 'no'  # 클래스 네임스페이스, 값이 다바뀜

print(Moblie.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)

realme.fp = 'realme change'  # 인스턴스 네임스페이스, 이 값만 바뀜

print(Moblie.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)