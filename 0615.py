


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value


stack = Stack()

stack.push(1)
stack.push(3)
stack.push(2)
stack.push(4)
stack.push(5)

for _ in range(5):
    print(stack.pop())


# 문제풀이

# def removeDuplicateLetters(self, s: str) -> str:

# stack = []
# for i in s:
#     if i in stack:
#         pass
#     else:
#         stack.append(i)

# # 재귀함수식 ??
# if not s:  # 빈문자열 보냈을때 예외처리
#     return ""

# for i in sorted(set(s)):
#     suffix = s[s.index(i):]
#     if set(s) == set(suffix):
#         return i + self.removeDuplicateLetters(suffix.replace(i, ""))

# return ""

# # 2
# def removeDuplicateLetters(self, s: str) -> str:
# 	if not s:
# 		return ""
#
# 	# 문자열의 문자 빈도수 계산
# 	counter = {char: 0 for char in set(s)}
#
# 	for char in s:
# 		counter[char] += 1
#
# 	# 사전순으로 가장 작은 문자의 인덱스 찾기
# 	min_idx = 0
# 	for i, char in enumerate(s):
# 		if char < s[min_idx]:
# 			min_idx = i
# 		counter[char] -= 1
# 		if counter[char] == 0:
# 			break
#
# 	return s[min_idx] + self.removeDuplicateLetters(s[min_idx + 1:].replace(s[min_idx], ""))

# 이게 할만함
def removeDuplicateLetters(self, s: str) -> str:
    last_occurrence = {c: i for i, c in enumerate(s)}
    stack = []
    in_stack = set()

    for i, c in enumerate(s):
        if c not in in_stack:
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                in_stack.remove(stack.pop())
            stack.append(c)
            in_stack.add(c)

    return "".join(stack)


# 스택으로 큐만들기

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# 큐로 스택만들기
import collections
class MyStack:

    def __init__(self):
        self.que = collections.deque()

    def push(self, x: int) -> None:
        self.que.append(x)
        for _ in range(len(self.que) - 1):
            self.que.append(self.que.popleft())

    def pop(self) -> int:
        return self.que.popleft()

    def top(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return len(self.que) == 0


# 원형 큐 구현

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen # 자리가 다차면 다시 0번으로 가니까 이렇게 계산하여 rear 처리
            return True
        else:
            False

    def deQueue(self) -> bool:  # 리턴 없이 삭제만
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.q[self.rear -1] is None else self.q[self.rear -1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None