
# # 클래스
# class Car:
# 	wheels = 4	# 클래스 속성
#
# 	def __init__(self, make, model, color):
# 		self.make = make
# 		self.model = model
# 		self.color = color
#
# 	# Method
# 	# @staticmethod  ???
# 	def drive(self):
# 		return "the car is moving"
#
# 	def stop(self):
# 		return f"the car {self.make} has stopped"
#
#
# my_car = Car("kia", "morning", "blue")
# print(my_car)
#
# #속성 사용하기
# print(my_car.make)
# print(my_car.wheels)
#
#
# #메소드 호출
# print(my_car.drive())
# print(my_car.stop())


# 부모 클래스
class Vehicle:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def start_engine(self):
		return "the engine is running"


class Car(Vehicle):
	def start_engine(self):
		return super().start_engine() + f" It's a {self.make} car engine"


#인스턴스 생성
my_car = Car("kia", "k3", "2023")

print(my_car.start_engine())



