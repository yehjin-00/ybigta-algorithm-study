## Title: 박스 채우기
## Number: 1493
## Date: 2021.11.03

L, W, H = map(int, input().split())
N = int(input())

cube = dict()
for i in range(N):
	a, b = map(int, input().split())
	cube[a] = b

total = 0
for n in list(cube):
	total += 2^(n*3) * cube[n]

if total < L*W*H:
	print(-1)
else:
	