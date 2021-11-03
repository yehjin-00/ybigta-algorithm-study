## Title: 회의실 배정
## Number: 1931
## Date: 2021.10.27

# 1. 같은 시간에 시작하는 회의들 중 끝나는 시간이 가장 빠른 것만 남긴다.
# 2. 제일 빠른 시간(0)부터 넣기 시작한다.
# 3. 다음 빠른 시간(1)이 앞선 회의(0)의 종료시간보다 늦거나 같게 시작하면 또 넣는다.
# 4. 만약 그렇지 않다면, 그 다음 회의(2)의 시작 시간이 제일 빠른 시간(0)의 종료 시간 이전인지 이후인지 확인한다.
# 5. 이전이면 (1)과 (2)를 택하며, 이후이면 (0)이나 (1) 중 아무거나 택한다.

N = int(input())
time = dict() # key: start time, value: end time
same = list() # start time, end time 같은 경우

for i in range(N):
	start, end = map(int, input().split())
	if start == end:
		same.append(start)  
	else:
		time[start] = min(time.get(start, end), end)

# start list, end list 구성 (같은 경우 제외)
start_list = sorted(list(time))
end_list = [time[v] for v in start_list]

# start, end 같은 경우 끼워넣기
start_list = sorted(list(time)+same)
for v in sorted(same):
    end_list.insert(start_list.index(v), v)

# 가장 빠른 회의 시간은 포함하고 시작
result = 1
i = 1
end_time = end_list[0]
while i < len(start_list):
	# 이전 회의 종료 시간 이후에 다음 회의가 시작되는 경우 추가
	if start_list[i] >= end_time: 
		end_time = end_list[i]
		result += 1
	# 이전 회의 중간에 시작하고 먼저 끝나는 경우 회의 바꾸기
	elif end_list[i] < end_time:
		end_time = end_list[i]
	# index update
	i += 1

print(result)