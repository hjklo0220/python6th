

s = "A man, a plan, a canal: Panama"

# # 1번 풀이
# from collections import deque
#
# class Solution:
# 	def isPalindrome(self, s: str) -> bool:
#
# 		answer = deque()
#
# 		for i in s:
# 			if i.isalnum():
# 				answer.append(i.lower())
#
# 		while len(answer) > 1:
# 			if answer.popleft() != answer.pop():
# 				return False
# 		return True

# # 2번 풀이
# import re
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#
#         s = s.lower()
#         s = re.sub('[^a-z0-9]', '', s)
#         return s == s[::-1]


# # 문자열 뒤집기
#
# s = ["h","e","l","l","o"]
#
# print(s[::-1])
# print(s.reverse())


# 로그 파일 재정렬

# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# # 람다 이용한 풀이
# letter_logs = []
# digit_logs = []
#
# for log in logs:
# 	if log.split()[1].isdigit():
# 		digit_logs.append(log)
# 	else:
# 		letter_logs.append(log)
#
# letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
# return letter_logs + digit_logs


# def custom_sort(log: str) -> tuple[str]:
# 	identifier, content = log.split(" ", 1)
# 	print(identifier, content)
# 	return content, identifier
#
#
# digits = []
# letters = []
# for log in logs:
# 	if log.split()[1].isdigit():
# 		digits.append(log)
# 	else:
# 		letters.append(log)
#
# letters.sort(key=custom_sort)
#
# print(letters + digits)



# # 가장 많이나온 단어
#
# import re
# import collections
#
#
# class Solution:
# 	def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
# 		words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
# 		.lower().split()
# 				 if word not in banned]
#
# 		counts = collections.Counter(words)
# 		return counts.most_common(1)[0][0]
#
#
# import re
# import collections
#
#
# class Solution:
# 	def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#
# 		words = re.findall(r'\w+', paragraph.lower())
#
# 		counts = collections.defaultdict(int)
# 		for word in words:
# 			if word not in banned:
# 				counts[word] += 1
#
# 		return max(counts, key=counts.get)


# # 문자열 배열을 받아 애너그램 단위로 그룹핑
#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         anagrams = {}
#         for word in strs:
#             sorted_word = "".join(sorted(word))
#             if sorted_word in anagrams:
#                 anagrams[sorted_word].append(word)
#             else:
#                 anagrams[sorted_word] = [word]
#         return anagrams.values()
#
# # 해시를 이용하는
#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         anagrams = {}
#         for word in strs:
#             count = [0] * 26
#             for c in word:
#                 count[ord(c) - ord('a')] += 1
#             key = tuple(count)
#             if key in anagrams:
#                 anagrams[key].append(word)
#             else:
#                 anagrams[key] = [word]
#         return anagrams.values()


# Timsort

def insertion_sort(arr, start, end):
	for i in range(start + 1, end + 1):
		key_item = arr[i]
		j = i - 1
		while j >= start and arr[j] > key_item:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j+1] = key_item

def merge(arr, start, mid, end):
	if arr[mid - 1] < arr[mid]:
		return

	left = arr[start:mid]
	right = arr[mid: end]

	k = start
	i = 0
	j = 0

	while (start + 1 < mid and mid + j < end):
		if(left[1] < right[j]):
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1

	if start + i < mid:
		arr[k:end] = left[i:]
	if mid + j < end:
		arr[k:end] = right[j:]


def timsort(arr):
	min_run = 32  # 최소 실행 횟수
	n = len(arr)  # 배열의 길이

	for i in range(0, n, min_run):
		insertion_sort(arr, i, min((i + min_run), n - 1))

	size = min_run
	while size < n:
		for start in range(0, n, size * 2):
			mid = start + size - 1
			end = min((start + size * 2 - 1), (n - 1))
			merge(arr, start, mid, end)

		size *= 2

	return arr


a = ['c', 'b', 'a', 'k', 'w', 'h', 'z', 's', '4', '6']

print(timsort(a))


# 강사님코드

def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key_item = arr[i]
        j = i - 1
        while j >= start and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item


def merge(arr, start, mid, end):
    if arr[mid] <= arr[mid + 1]:
        return

    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


def timsort(arr):
    min_run = 4
    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(start + size - 1, n - 1)
            end = min(start + 2 * size - 1, n - 1)
            merge(arr, start, mid, end)
        size *= 2

    return arr


a = ['f', 'g', 'h', 'z', 's', 'b', 'c', 'd']

print(timsort(a))