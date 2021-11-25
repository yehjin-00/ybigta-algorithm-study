## Title: 중앙값 구하기
## Number: 2696
## Date: 2021.11.24

import heapq
import sys

N = int(sys.stdin.readline())
for _ in range(N):
	n = int(sys.stdin.readline())
	cmds = list()

	for i in range((n-1)//10+1):
		cmds += list(map(int, sys.stdin.readline().split()))
	
	left, right = [], []
	result = []
	for i in range(n):
		cmd = cmds[i]
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

		if i%2==0: result.append(-left[0])

	print(len(result))
	for i in range(len(result)):
		if i != 0 and i%10==0 or i==len(result)-1: print(result[i])
		else: print(result[i], end=' ')