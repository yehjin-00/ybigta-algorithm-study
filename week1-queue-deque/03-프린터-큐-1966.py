## Title: 프린터 큐
## Number: 1966
## Date: 2021.09.22

import sys

n = int(sys.stdin.readline())

for i in range(n):
	size, idx = map(int, sys.stdin.readline().split())
	queue = list(map(int, sys.stdin.readline().split()))

	result = 1
	while idx != 0 or queue[idx] != max(queue):
		if queue[0] == max(queue):
			idx -= 1
			result += 1
			queue.pop(0)
		elif idx == 0:
			queue.append(queue.pop(0))
			idx = len(queue)-1
		else:
			queue.append(queue.pop(0))
			idx -= 1

	print(result)