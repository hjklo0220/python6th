import random
import time

menu = ["된장찌개", "피자", "제육볶음", "짜장면"]
while True:
	print(menu)
	food = input("추가할 매뉴를 입력하세요 (끝내기: q) :")
	if food == 'q':
		break
	else:
		menu.append(food)
print(menu)

set_menu = set(menu)
while True:
	food = input("삭제할 매뉴를 입력하세요 (끝내기: q) :")
	if food == 'q':
		break
	else:
		# del menu[menu.index(food)]
		set_menu = set_menu - {food}
	print(set_menu)

print(f"매뉴 리스트 : {set_menu}")

for i in range(5, 0, -1):
	print(i)
	time.sleep(1)

print(f"오늘의 매뉴는 [{random.choice(list(set_menu))}] 입니다")



