# # 변수 선언
# a = 10
# b = 3.14
# c = 'hello world'
# d = [1, 2, 3]
# e = (4, 5, 6)  # 튜플
# f = {7, 8, 9}  # set(집합) 유니크 보장되어있음
# g = {"apple": 1,
#      "banana": 2,
#      "orange": 3
#      }
#
# print(type(a), a)
# print(type(b), b)
# print(type(c), c)
# print(type(d), d)
# print(type(e), e)
# print(type(f), f)
# print(type(g), g)

# # 산술 연산자
# a = 4
# b = 2
# total = a + b
# print("a + b = ", total)
# total = a - b
# print("a - b = ", total)
# total = a * b
# print("a * b = ", total, type(total))
# print("a / b = ", total, type(a / b))
#
# a = 5
# b = 2
# print("a % b = ", a % b)
# print("a ** b = ", a ** b)
# print("a // b = ", a // b) # 몫(양수)
# a = -5
# print("a // b = ", a // b) # 몫(음수)


# # 비교 연산자
# a = 5
# b = 2
# print(f'{a} < {b} : ', a < b)
# print(f'{a} <= {b} : ', a <= b)
# print(f'{a} == {b} : ', a == b)
# print(f'{a} != {b} : ', a != b)

# 논리연산자
a = 5
b = 2
c = 3
d = 200
print(f'{a} > {b} and {a} > {c} : ', a > b and a > c)
print(f'{a} > {b} and {a} < {c} : ', b < a < c)  # 메소트 체이닝 : 파이썬이 스크립트언어라서 가능

print(f'{a} > {b} or {a} > {c} : ', a > b or a < c)

print(f'not({a} < {b}) : ', not (a < b))
