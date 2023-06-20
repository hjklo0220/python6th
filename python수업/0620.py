import collections


# # 그래프 문제1
# # 풀이 1
# def letterCombinations(self, digits):
# 	if not digits:
# 		return []
#
# 	phone = {"2": "abc", "3": "def",
# 			 "4": "ghi", "5": "jkl", "6": "mno",
# 			 "7": "pqrs", "8": "tuv", "9": "wxyz"}
# 	res = []
#
# 	def backtrack(combination, next_digits):
# 		if not next_digits:
# 			res.append(combination)
# 			return
#
# 		for letter in phone[next_digits[0]]:
# 			backtrack(combination + letter, next_digits[1:])
#
# 	backtrack("", digits)
# 	return res
#
# # 풀이2
#
# def letterCombinations(self, digits):
# 	def dfs(index, path):
# 		if len(path) == len(digits):
# 			result.append(path)
# 			return
# 		for i in range(index, len(digits)):
# 			for j in dic[digits[i]]:
# 				dfs(i + 1, path + j)
#
# 	if not digits:
# 		return []
#
# 	dic = {"2": "abc", "3": "def",
# 		   "4": "ghi", "5": "jkl", "6": "mno",
# 		   "7": "pqrs", "8": "tuv", "9": "wxyz"}
# 	result = []
#
# 	dfs(0, "")
#
# 	return result
#
#
# # 문제2
#
# def permute(self, nums):
# 	def dfs(path):
# 		if len(path) == len(nums):
# 			result.append(path[:])
# 			return
# 		for i in range(len(nums)):
# 			if nums[i] in path:
# 				continue
# 			dfs(path + [nums[i]])
#
# 	result = []
# 	dfs([])
# 	return result
#
#
# # 문제 3
# # https://leetcode.com/problems/reconstruct-itinerary/description/
# from collections import defaultdict
# def findItinerary(self, tickets: List[List[str]]) -> List[str]:
# 	graph = defaultdict(list)
#
# 	for src, dst in sorted(tickets):  # 티켓 정렬
# 		graph[src].append(dst)
#
# 	route = []
#
# 	def visit(city):
# 		while graph[city]:
# 			next_city = graph[city].pop(0)
# 			visit(next_city)
# 		route.append(city)
#
# 	visit("JFK")
# 	return route[::-1]

# 풀이2

def findItinerary(self, tickets):

	graph = collections.defaultdict(list)
	print(graph)

	for a, b in sorted(tickets):
		graph[a].append(b)

	route = []
	stack = ["JFK"]

	while stack:
		while graph[stack[-1]]:
			stack.append(graph[stack[-1]].pop(0))
		route.append(stack.pop())

	return route[::-1]


# 최단경로 문제
# https://leetcode.com/problems/network-delay-time/description/
# 다익스트라 알고리즘 풀이

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
	graph = collections.defaultdict(list)
	for u, v, w in times:
		graph[u].append((v, w))  # ((실제 경로, 가중치))

	Q = [(0, k)]
	dist = collections.defaultdict(int)

	while Q:
		time, node = heapq.heappop(Q)
		if node not in dist:
			dist[node] = time
			for v, w in graph[node]:
				alt = time + w
				heapq.heappush(Q, (alt, v))

	if len(dist) == n:
		return max(dist.values())

	return -1