## Title: 소가 길을 건너간 이유 4
## Number: 14464
## Date: 2021.11.24


# 소 포함 관계일때 문제
import heapq
import sys

C, N = map(int, sys.stdin.readline().split())

T = []
for _ in range(C):
	heapq.heappush(T, int(sys.stdin.readline()))

AB = []
for _ in range(N):
	a, b = map(int, sys.stdin.readline().split())
	heapq.heappush(AB, (b, a))

result = 0
while AB:
	chicken = heapq.heappop(T)
	cow = heapq.heappop(AB)
	while T and chicken > cow[0]:
		chicken = heapq.heappop(T)
	if chicken > cow[0]: break
	
	if chicken >= cow[1]:
		result += 1
		if T: chicken = heapq.heappop(T)

print(result)

# 소 포함 관계일때 문제
import heapq
from queue import Queue
import sys

C, N = map(int, sys.stdin.readline().split())

T = []
for _ in range(C):
	heapq.heappush(T, int(sys.stdin.readline()))

AB = []
for _ in range(N):
	a, b = map(int, sys.stdin.readline().split())
	# heapq.heappush(AB, (a, b))
	AB.append((a, b))

AB = sorted(AB, key=lambda x: (x[1], x[0]))

result = 0
tmp_cow = list()
chicken = heapq.heappop(T)
# 남은 소가 있을 때까지 반복
while AB:
	cow = AB.pop(0)
	# 시작 시간이 가장 빠른 소보다 앞의 닭들 보내기
	while T and chicken < cow[0]: 
		chicken = heapq.heappop(T)
	
	# 닭이 더 이상 없다면 break
	if chicken < cow[0]: break
    
    # 현재 소를 도울 수 있는 닭이 있다면,
	if chicken <= cow[1]:
		# 현재 소의 정보 keep
		i = 1
		start, end = cow
		# 현재 소의 시간에 다음 소의 시간이 포함된다면, 가장 안쪽 소 찾기
		while i<len(AB) and start<=AB[i][0] and end>=AB[i][1] and AB[i][0]<=chicken and AB[i][1]>=chicken:
			i += 1
		
		result += 1

		# 남은 닭이 있다면 다음 닭 소환, 남은 닭 없으면 종료
		if T: chicken = heapq.heappop(T)
		else: break

print(result)

# 포기.