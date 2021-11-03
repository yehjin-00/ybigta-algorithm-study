## Title: 강의실 배정
## Number: 11000
## Date: 2021.11.03

import heapq

N = int(input())
time = list() 

for i in range(N):
	start, end = map(int, input().split())
	time.append([start, end])  

time.sort(key = lambda x:x[0])

table = [time[0][1]]
i = 1
while i < len(time):
	if time[i][0] < table[0]:
		heapq.heappush(table, time[i][1])
	else:
		heapq.heappop(table)
		heapq.heappush(table, time[i][1])
	i += 1

print(len(table))