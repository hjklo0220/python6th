# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# # https://leetcode.com/problems/linked-list-cycle/submissions/
#
# def hasCycle(self, head: Optional[ListNode]) -> bool:
#
#         node_seen = set()
#         while head is not None:
#             if head in node_seen:
#                 return True
#             node_seen.add(head)
#             head = head.next
#         return False
#
# def hasCycle(self, head: Optional[ListNode]) -> bool:
#
#         if not head or not head.next:
#             return False
#
#         slow = head
#         fast = head.next
#
#         while slow != fast:
#             if not fast or not fast.next:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True


# 그래프
# DFS 순회
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()

def dfs_iterative(start_node):
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))


snode = 'A'
dfs_iterative(snode)


# # https://leetcode.com/problems/number-of-islands/description/
#
# def numIslands(self, grid: List[List[str]]) -> int:
#     m = len(grid)
#     n = len(grid[0])
#     answer = 0
#
#     def dfs(i, j):
#         if grid[i][j] == "1":
#             grid[i][j] = "x"
#             if j < n - 1:
#                 dfs(i, j + 1)
#             if j > 0:
#                 dfs(i, j - 1)
#             if i > 0:
#                 dfs(i - 1, j)
#             if i < m - 1:
#                 dfs(i + 1, j)
#
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j] == "1":
#                 answer += 1
#                 dfs(i, j)
#
#     return answer
#
# # 풀이2
#
# def numIslands(self, grid: List[List[str]]) -> int:
#
#     def dfs(grid, i, j):
#         if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
#             return
#         grid[i][j] = '0'
#         dfs(grid, i - 1, j)
#         dfs(grid, i + 1, j)
#         dfs(grid, i, j - 1)
#         dfs(grid, i, j + 1)
#
#     count = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] == "1":
#                 dfs(grid, i, j)
#                 count += 1
#     return count

