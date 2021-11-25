## Title: 가운데를 말해요
## Number: 1655
## Date: 2021.11.24

import heapq
import sys

left = [] # 최대힙
right = [] # 최소힙

n = int(sys.stdin.readline())

for i in range(n):
	cmd = int(sys.stdin.readline())
	if i == 0:
		heapq.heappush(left, -cmd)
	elif len(left)==len(right) and -left[0] <= cmd:
		heapq.heappush(left, -heapq.heappushpop(right, cmd))
	elif len(left)==len(right) and -left[0] > cmd:
		heapq.heappush(left, -cmd)
	elif -left[0] <= cmd:
		heapq.heappush(right, cmd)
	else:
		heapq.heappush(right, -heapq.heappushpop(left, -cmd))

	print(-left[0])