## Title: 요세푸스 문제 0
## Number: 11866
## Date: 2021.09.22

import sys
input = sys.stdin.readline
N, step = map(int, input().split())

yos = list(range(1, N+1))
result = []

n = 0
while len(yos) > 0:
	n += step-1
	n = n % len(yos)
	result.append(str(yos.pop(n)))

print('<'+', '.join(result)+'>')