## Title: 덱
## Number: 10866
## Date: 2021.09.22

import sys

n = int(sys.stdin.readline())
deque = []

for i in range(n):
	order = sys.stdin.readline().split()
	if order[0] == "push_back": deque.append(order[1])

	elif order[0] == "push_front": deque.insert(0, order[1])

	elif order[0] == "size": print(len(deque))

	elif order[0] == "empty":
		if len(deque) == 0: print(1)
		else: print(0)

	elif len(deque) == 0: print(-1)

	elif order[0] == "pop_front": print(deque.pop(0))

	elif order[0] == "pop_back": print(deque.pop())

	elif order[0] == "front": print(deque[0])

	elif order[0] == "back": print(deque[-1])

