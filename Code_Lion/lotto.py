import random

count = int(input("구매할 로또 갯수 :"))

for i in range(count):
	print(sorted(random.sample(range(1, 46), 6)))