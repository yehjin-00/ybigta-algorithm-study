## Title: 부분 수열의 합
## Number: 1182
## Date: 2021.10.06

import itertools

N, S = map(int, input())
lst = list(map(int, input()))

result = 0
for i in range(1, N+1):
	combi = itertools.combinations(lst, i)
	for c in combi:
		if sum(lst) == S: result += 1