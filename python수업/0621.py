
# 트리

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs풀이
def maxDepth(self, root: Optional[TreeNode]) -> int:

	def dfs(root, depth):
		if not root:
			return depth
		return max(dfs(root.left, depth+1), dfs(root.right, depth + 1))

	return dfs(root, 0)

# 풀이 2 큐를활용
def maxDepth(self, root: Optional[TreeNode]) -> int:
	if root is None:
		return 0

	queue = collections.deque([root])
	depth = 0

	while queue:
		depth += 1
		for _ in range(len(queue)):
			current_root = queue.popleft()
			if current_root.left:
				queue.append(current_root.left)
			if current_root.right:
				queue.append(current_root.right)

	return depth
# 문제 2
# https://leetcode.com/problems/longest-univalue-path/submissions/

def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
	self.longest_path = 0

	def dfs(node):
		if not node:
			return 0

		left_length = dfs(node.left)
		right_length = dfs(node.right)

		left_arrow = right_arrow = 0

		if node.left and node.left.val == node.val:
			left_arrow = left_length + 1
		if node.right and node.right.val == node.val:
			right_arrow = right_length + 1

		self.longest_path = max(self.longest_path, left_arrow + right_arrow)

		return max(left_arrow, right_arrow)

	dfs(root)
	return self.longest_path



# 문제 3
# https://leetcode.com/problems/balanced-binary-tree/submissions/975981269/
def isBalanced(self, root: Optional[TreeNode]) -> bool:
	def check_height(node):
		if not node:
			return 0

		left_height = check_height(node.left)
		right_height = check_height(node.right)

		if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
			return -1

		return max(left_height, right_height) + 1

	return check_height(root) != -1

# def dfs(root):
#     if not root:
#         return [True, 0]
#     left = dfs(root.left)
#     right = dfs(root.right)
#     balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
#     return [balance, 1 + max(left[1], right[1])]

# res = dfs(root)
# return res[0]


# 문제 4
#https://leetcode.com/problems/minimum-height-trees/submissions/975990317/

def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
	if n <= 1:
		return [0]

	graph = collections.defaultdict(list)
	for i, j in edges:
		graph[i].append(j)
		graph[j].append(i)

	leaves = []
	for i in range(n + 1):
		if len(graph[i]) == 1:
			leaves.append(i)

	while n > 2:
		n -= len(leaves)
		new_leaves = []

		for leaf in leaves:
			neighbor = graph[leaf].pop()
			graph[neighbor].remove(leaf)

			if len(graph[neighbor]) == 1:
				new_leaves.append(neighbor)
		leaves = new_leaves

	return leaves


# 이진 탐색 트리
# 문제 5
# https://leetcode.com/problems/range-sum-of-bst/description/

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
	# recursive DFS
	# a = []
	# def dfs(node):
	#     if not node:
	#         return
	#     if low <= node.val <= high:
	#         a.append(node.val)
	#     dfs(node.left)
	#     dfs(node.right)
	# dfs(root)
	# return sum(a)

	# DFS
	stack = [(root, root.val)]
	a = 0
	while stack:
		node, val = stack.pop()
		if low <= val <= high:
			a += val
		if node.left:
			stack.append((node.left, node.left.val))
		if node.right:
			stack.append((node.right, node.right.val))
	return a

	# BSF

	# d = collections.deque([(root, root.val)])
	# a = 0
	# while d:
	#     node, val = d.popleft()
	#     if low <= val <= high:
	#         a += val
	#     if not ( node.left or node.right):
	#         continue
	#     if node.left:
	#         d.append((node.left, node.left.val))
	#     if node.right:
	#         d.append((node.right, node.right.val))
	# return a


# 풀이 2

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.answer = 0

        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.answer += node.val
                if low < node.val:
                    dfs(node.left)
                if high > node.val:
                    dfs(node.right)

        dfs(root)
        return self.answer