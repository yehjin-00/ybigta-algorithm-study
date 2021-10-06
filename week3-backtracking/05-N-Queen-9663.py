## Title: N Queen
## Level: 14_05
## Number: 9663
## Date: 2021.10.07


## deep copy를 이용한 풀이

import copy
def check(line, where, chess):
	for i in range(len(chess)):
		for j in range(len(chess)):
			if i == line or j == where or i+j==line+where or i-j==line-where:
				chess[i][j] = -1

def queen(line, l_max, chess, result):   
	if line==l_max:
		if 1 in chess[line]:
			result.append(1)
	else:
		for i in range(len(chess)):
			if chess[line][i] > 0:               
				c = copy.deepcopy(chess)
				check(line, i, c)              
				queen(line+1, l_max, c, result)

n = int(input())

chess = [[1 for i in range(n)] for i in range(n)]
result = []
queen(0, n-1, chess, result)
print(sum(result))


## 원 상태로 돌리기 위한 방안 2 (back function 구현)

def back(chess, threshold):
	for i in range(len(chess)):
		for j in range(len(chess)):
			if chess[i][j] == -threshold:
				chess[i][j] = 1

def check(line, where, chess, num):
	for i in range(len(chess)):
		for j in range(len(chess)):
			if (i == line or j == where or i+j==line+where or i-j==line-where) and chess[i][j]==1:
				chess[i][j] = -num
            

def queen(line, l_max, chess, result):  
	if line==l_max:
		if 1 in chess[line]:
			result.append(chess)
	elif 1 in chess[line]:
		for i in range(len(chess)):
			check_num = l_max * line
			if chess[line][i] > 0:               
				check(line, i, chess, check_num)              
				queen(line+1, l_max, chess, result)
				back(chess, check_num)

n = int(input())
chess = [[1 for i in range(n)] for i in range(n)]
result = []
queen(0, n-1, chess, result)
print(sum(result))


## 구조 자체를 바꾼 시도

def check(x, y, chess):
    for a, b in chess:
        if x == a or b == y or a+b == x+y or a-b == x-y:
            return False
    return True

def queen(line, N, chess, result):
    for i in range(N):
        if check(line, i, chess):
            chess.append([line, i])
            if line==N-1:
                result.append(1)
            else:
                queen(line+1, N, chess, result)
            chess.pop()

n = int(input())
chess = []
result = []
queen(0, n, chess, result)
print(sum(result))


## 모든 경우 파악

import itertools
n = int(input())
perm = itertools.permutations(range(n), n)
result = 0
for case in perm:
	i = 1
	stop = True
	while i < n:
		start = i
		while start < n:
			if case[start]-case[start-i] in (i, -i): 
				start = n
				stop = False
			start += 1
		i += 1
		if not stop: i = n
	if stop: 
		result += 1
print(result)



## 성공
# cProfile 돌려보니까 check에 소요되는 시간이 너무 많아 최대한 비교 횟수를 줄이려고 노력
def check(x, y, chess):
    for i in range(len(chess)):
        if i+chess[i] == x+y: return False
        if i-chess[i] == x-y: return False
    return True

def queen(line, N, chess, result):
    for i in range(N):
        if i not in chess and check(line, i, chess):
            chess.append(i)
            if line==N-1:
                result.append(1)
            else:
                queen(line+1, N, chess, result)
            chess.pop()

n = int(input())
chess = []
result = []
queen(0, n, chess, result)
print(sum(result))






n = 01, solution count is 1.
n = 02, solution count is 0.
n = 03, solution count is 0.
n = 04, solution count is 2.
n = 05, solution count is 10.
n = 06, solution count is 4.
n = 07, solution count is 40.
n = 08, solution count is 92.
n = 09, solution count is 352.
n = 10, solution count is 724.
n = 11, solution count is 2680.
n = 12, solution count is 14200.
n = 13, solution count is 73712.







