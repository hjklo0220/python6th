# # 문제 1

nums = [2,7,11,15]
target = 9

# # 시간복잡도 On^2
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#
# 	for i in range(len(nums)):
# 		for j in range(i + 1, len(nums)):
# 			if nums[i] + nums[j] == target:
# 				return [i, j]
#
# # 다른풀이
#
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#
#         for i, n in enumerate(nums):
#             complement = target - n
#             if complement in nums[i+1:]:
#                 return [i, nums[i+1:].index(complement) + (i + 1)]

#다른풀이
# 가장 빠름 역 색인
def twoSum(self, nums: list[int], target: int) -> list[int]:

        num_map = {}
        for i, num in enumerate(nums):
            num_map[num] = i


        for i, num in enumerate(nums):
            if target - num in num_map and num_map[target-num] != i:
                return [i, num_map[target-num]]



# 떨어지는 물 받기

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# def trap(self, height: list[int]) -> int:
#     if not height:
#         return 0
#
#     volume = 0  # 물 저장
#     left, right = 0, len(height) - 1  # 포인터 지정 양끝에
#     left_max, right_max = height[left], height[right]
#
#     while left < right:
#         left_max = max(height[left], left_max)
#         right_max = max(height[right], right_max)
#
#         if left_max <= right_max:
#             volume += left_max - height[left]
#             left += 1
#         else:
#             volume += right_max - height[right]
#             right -= 1
#
#     return volume


# 연결 리스트(Linked list)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        q = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


# deque를 사용한 풀이
import collections


def isPalindrome(self, head: Optional[ListNode]) -> bool:
    q = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True

# 러너 방식

def isPalindrome(self, head: Optional[ListNode]) -> bool:

    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


# 연결 리스트 뒤집기
# 풀이1
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node = head
    prev = None

    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev

# 풀이2 재귀

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)
