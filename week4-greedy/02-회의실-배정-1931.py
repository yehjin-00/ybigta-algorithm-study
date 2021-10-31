## Title: 회의실 배정
## Number: 1931
## Date: 2021.10.27

N = int(input())
time = list()
for i in range(N):
	time.append(list(map(int, input().split())))


# 1. 같은 시간에 시작하는 회의들 중 끝나는 시간이 가장 빠른 것만 남긴다.
# 2. 제일 빠른 시간(0)부터 넣기 시작한다.
# 3. 다음 빠른 시간(1)이 앞선 회의(0)의 종료시간보다 늦거나 같게 시작하면 또 넣는다.
# 4. 만약 그렇지 않다면, 그 다음 회의(2)의 시작 시간이 제일 빠른 시간(0)의 종료 시간 이전인지 이후인지 확인한다.
# 5. 이전이면 (1)과 (2)를 택하며, 이후이면 (0)이나 (1) 중 아무거나 택한다.

sorted(str_list, key=lambda x : x[1]) 


min(a.get('a', 0), 0)
