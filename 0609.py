# # 클래스 네임스페이스, 인스턴스 네임스페이스 차이
# class Moblie:
# 	fp = "yes"
#
#
# realme = Moblie()  # 생성자 함수, 이 클래스를
# redme = Moblie()
# geek = Moblie()
#
# print(Moblie.fp)
# print(realme.fp)
# print(redme.fp)
# print(geek.fp)
#
#
# Moblie.fp = 'no'  # 클래스 네임스페이스, 값이 다바뀜
#
# print(Moblie.fp)
# print(realme.fp)
# print(redme.fp)
# print(geek.fp)
#
# realme.fp = 'realme change'  # 인스턴스 네임스페이스, 이 값만 바뀜
#
# print(Moblie.fp)
# print(realme.fp)
# print(redme.fp)
# print(geek.fp)
import time


# # 메소드 오버라이딩
#
# class Vector(object):
# 	def __init__(self, x, y):  # 생성자 함수 Vector() 하면 실행되는거임
# 		self.x = x
# 		self.y = y
#
# 	def __add__(self, other):  # 연산자 오버로딩 ,정의를 해야만 쓸수 있음 오브젝트 클래스에 정의가 안되어있음
# 		return Vector(self.x + other.x, self.y + other.y)
#
# 	def __str__(self):  # 오브젝트 클래스에 정의되어있음, 새로 내맘대로 정의한것임 -> 오버라이딩
# 		return f'Vertor({self.x}, {self.y})'
#
#
#
# a = Vector(1, 2)  # 인스턴스 네임스페이스
# b = Vector(3, 4)
#
# print(a)
# print(b)
#
# c = a + b
#
# print(c)


# time 모듈
# import time
# print(time.time())
# print(time.ctime())

# from datetime import datetime
# from datetime import date
#
# dt = datetime(year=2023, month=5, day=5, hour=10, minute=30)
# print(dt, type(dt))
#
# current_time = time.ctime()
# current_datetime = datetime.now()
# print(current_time, current_datetime)  # 날짜 시간 전부
#
# d = date(year=2023, month=6, day=25)
# print(d)  # 날짜만
#
# current_date = date.today()
# print(current_date)

from datetime import timedelta

td = timedelta(days=10)
print(td)

from datetime import date

d1 = date(year=2023, month=5, day=5)
d2 = date(year=2023, month=6, day=9)

# 날짜의 연산자 오버로딩으로 비교가능
print(d1 == d2)
print(d1 < d2)
print(d1 > d2)

from datetime import datetime

dt = datetime.today()

formated_datetime = dt.strftime('%B, %d, %Y')  # 포멧코드로 포멧팅한 문자를 만들어주는 메소드
print(formated_datetime)

# class ParentClass:
#
# 	def __init__(self):
# 		self.name = 'parent'
# 		self.number = 10
#
# 	def __str__(self):
# 		return f"ParentClass name : {self.name}, number : {self.number}"
#
# 	def add_num(self, new_number):
# 		print('부모 : ', new_number, '만큼 더해라')
# 		self.number = self.number + new_number
#
#
# class ChildCloass(ParentClass):
# 	def __init__(self):
# 		super().__init__()  # super은 부모클래스를 의미함
# 		self.name = "child"
#
# 	def __str__(self):
# 		return f"ChildClass name : {self.name}, number : {self.number}"
#
# 	def add_num(self, new_number):
# 		print("말 안듣는 자식: 고정적으로 5더할거임")
# 		self.number = self.number + 5
#
#
# parent = ParentClass()
# child = ChildCloass()
# print(parent)
# print(child)
#
# print(" + 7")
# parent.add_num(7)
# child.add_num(7)
# print(parent)
# print(child)

