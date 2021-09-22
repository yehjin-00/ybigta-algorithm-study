## Title: 회전하는 큐
## Number: 1021
## Date: 2021.09.22

from collections import deque
import sys

input = sys.stdin.readline
size, n = map(int, input().split())
targets = list(map(int, input().split()))
deq = deque(range(1, size+1))

result = 0
for target in targets:
	if target == deq[0]:
		deq.popleft()

	elif deq.index(target) < len(deq)/2:
		for i in range(deq.index(target)):
			deq.append(deq.popleft())
			result += 1
		deq.popleft()

	else:
		for i in range(len(deq)-deq.index(target)):
			deq.appendleft(deq.pop())
			result += 1
		deq.popleft()

print(result)