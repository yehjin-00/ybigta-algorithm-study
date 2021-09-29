## Title: 뱀
## Number: 3190
## Date: 2021.09.29

from collections import deque
import sys

N = int(input())

# 사과 지도
apple = [[False for i in range(N)]for j in range(N)]
snake = [[False for i in range(N)]for j in range(N)]

# 사과 개수
n = int(input())

# 사과 위치 표시
for i in range(n):
	row, col = map(int, input().split())
	apple[row-1][col-1] = True

# 뱀 위치 deque
row, col = 0, 0
deq = deque([(row, col)])

# 방향 (위 0, 오른쪽 1, 아래쪽 2, 왼쪽 3)
direction = 1

# 방향별 앞으로 가자!
def next_place(row, col):
	if direction == 0:
		return (row-1, col)
	elif direction == 1:
		return (row, col+1)
	elif direction == 2:
		return (row+1, col)
	elif direction == 3:
		return (row, col-1)

# 이동 횟수
n = int(input())
result = 0
done = False
num = 0

# 뱀 위치 표시
for i in range(n):
	next_num, next_direction = input().split()
	if not done:
		for i in range(int(next_num)-num):
			row, col = next_place(row, col)
			if row < 0 or row > N-1 or col < 0 or col > N-1 or snake[row][col]:
				result += 1
				done = True
				break                
			elif apple[row][col]:
				apple[row][col] = False
				snake[row][col] = True
				deq.append((row, col))
				result += 1  
			else:
				deq.append((row, col))
				pop_row, pop_col = deq.popleft()
				snake[pop_row][pop_col] = False  
				snake[row][col] = True
				result += 1 
		num = int(next_num)            
		if next_direction == 'D':
			direction += 1
			direction %= 4
		else:
			direction -= 1
			direction %= 4

if not done:
    row, col = next_place(row, col)
    while row>=0 and row<N and col>=0 and col<N and not snake[row][col]:   
        result += 1  
        row, col = next_place(row, col)
    result += 1

print(result)



