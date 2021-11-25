## Title: 최대 힙
## Number: 11279
## Date: 2021.11.24

import heapq
import sys

n = int(sys.stdin.readline())
q = []

for i in range(n):
	cmd = int(sys.stdin.readline())
	if cmd != 0:
		heapq.heappush(q, -cmd)
	elif q:
		print(-heapq.heappop(q))
	else:
		print(0)