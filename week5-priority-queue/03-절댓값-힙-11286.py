## Title: 절댓값 힙
## Number: 11286
## Date: 2021.11.24

import heapq
import sys

n = int(sys.stdin.readline())
q = []

for i in range(n):
	cmd = int(sys.stdin.readline())
	if cmd != 0:
		heapq.heappush(q, (abs(cmd), cmd))
	elif q:
		print(heapq.heappop(q)[1])
	else:
		print(0)