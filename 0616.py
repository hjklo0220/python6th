
# CircularDeque

class MyCircularDeque:

	def __init__(self, k: int):
		self.head = ListNode(None)
		self.tail = ListNode(None)
		self.k = k
		self.len = 0
		self.head.right = self.tail
		self.tail.left = self.head

	def _add(self, node: ListNode, new: ListNode):
		n = node.right
		node.right = new
		new.left = node
		new.right = n
		n.left = new

	def _del(self, node: ListNode):
		n = node.right.right
		node.right = n
		n.left = node

	def insertFront(self, value: int) -> bool:
		if self.len == self.k:
			return False
		self.len += 1
		self._add(self.head, ListNode(value))
		return True

	def insertLast(self, value: int) -> bool:
		if self.len == self.k:
			return False
		self.len += 1
		self._add(self.tail.left, ListNode(value))
		return True

	def deleteFront(self) -> bool:
		if self.len == 0:
			return False
		self.len -= 1
		self._del(self.head)
		return True

	def deleteLast(self) -> bool:
		if self.len == 0:
			return False
		self.len -= 1
		self._del(self.tail.left.left)
		return True

	def getFront(self) -> int:
		return self.head.right.val if self.len else -1

	def getRear(self) -> int:
		return self.tail.left.val if self.len else -1

	def isEmpty(self) -> bool:
		return self.len == 0

	def isFull(self) -> bool:
		return self.len == self.k


# heap

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

# 해쉬테이블

class ListNode:
	def __init__(self, key=None, value=None):
		self.key = key
		self.value = value
		self.next = None


class MyHashMap:

	def __init__(self):
		self.size = 1000
		self.table = collections.defaultdict(ListNode)

	def put(self, key: int, value: int) -> None:
		index = key % self.size
		if self.table[index].value is None:
			self.table[index] = ListNode(key, value)
			return

		p = self.table[index]
		while p:
			if p.key == key:
				p.value = value
				return
			if p.next is None:
				break
			p = p.next
		p.next = ListNode(key, value)

	def get(self, key: int) -> int:
		index = key % self.size
		if self.table[index].value is None:
			return -1
		p = self.table[index]
		while p:
			if p.key == key:
				return p.value
			p = p.next
		return -1

	def remove(self, key: int) -> None:
		index = key % self.size
		if self.table[index].value is None:
			return
		p = self.table[index]
		if p.key == key:
			self.table[index] = ListNode() if p.next is None else p.next
			return

		prev = p
		while p:
			if p.key == key:
				prev.next = p.next
				return
			prev, p = p, p.next