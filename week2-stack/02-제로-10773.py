## Title: 제로
## Number: 10773
## Date: 2021.09.30

import sys

n = int(sys.stdin.readline())
stack = list()
size = 0

for i in range(n):
	num = int(sys.stdin.readline())
	if num == 0:
		size -= 1
	else:
		stack.insert(size, num)
		size += 1

print(sum(stack[:size]))