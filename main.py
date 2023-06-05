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

# # 논리연산자
# a = 5
# b = 2
# c = 3
# d = 200
# print(f'{a} > {b} and {a} > {c} : ', a > b and a > c)
# print(f'{a} > {b} and {a} < {c} : ', b < a < c)  # 메소트 체이닝 : 파이썬이 스크립트언어라서 가능
#
# print(f'{a} > {b} or {a} > {c} : ', a > b or a < c)
#
# print(f'not({a} < {b}) : ', not (a < b))

# # 할당 연산자 =
# a = 10
# b = 20
# m = 15
#
# y = a + b
# print(y)
# m += 10
# print(m)
#
# m **= 2
# print(m)
#
# m //= 10
# print(m)

# # 비트연산자
# a = 10
# b = 15
#
# print('a: ', bin(a))  # 0b: 2진수, 0x: 16진수
# print('a: ', hex(a))
# print('b: ', bin(b))
# print('~b : ', ~b, bin(~b))
#
# print(f'{a} & {b}  : ', a & b, bin(a&b))
# print(f'{a} << 2  : ', a << 2, bin(a<<b))
# print(f'{a} >> 2  : ', a >> 2, bin(a>>b))


# # 맴버 in 연산자
# s1 = "Welcome to Python"
# print("to" in s1)
# s2 = "Welcome top python"
# print('to' in s2)
# s3 = "Welcome to Python"
# print('wel' in s3)  # 대소문자 구문함
#
# print('to' not in s3)


# # is 연산자
# a = 10
# b = 10
# print(a is b)
#
# a = 10
# b = '10'
# print(a is b)
# print(a is not b)


# 타입 변환
# # 암시적 타입 변환 (동적 타입핑)
# a = 5
# b = 2
# print(b, type(b))
# value = a / b
# print(value, type(value))
#
# x = 10
# y = 5.5
# total = x + y
# print("x + Y =", total, type(total))
#
# j = "hello"
# k = "world"
# p = j + k
# print(p, type(p))
#
# q = 20
# u = '10'
# r = q + u   # 오류
# print(r, type(r))

# 명시적 타입 변환 (개발자가 의도해서 변경)
a = 5
b = 2
value = a / b
print(value, type(value))
int_value = int(value)
print(int_value, type(int_value))

q = 20
u = '10'
print(u, type(u))
r = q + int(u)
print(r, type(r))



