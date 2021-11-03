## Title: 스도쿠
## Number: 2580
## Date: 2021.11.03

sudoku = [list(map(int, input().split())) for i in range(9)]

def possible(x, y):
	num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	# 가로 세로 확인
	for i in range(9):
		if sudoku[x][i] in num: num.remove(sudoku[x][i])
		if sudoku[i][y] in num: num.remove(sudoku[i][y])

	# 3*3 확인
	n = x // 3
	m = y // 3

	for i in range(n*3, n*3+3):
		for j in range(m*3, m*3+3):
			if sudoku[i][j] in num:
				num.remove(sudoku[i][j])
	return num

def backtracking(idx):
	if idx < 81:
		for i in range(idx, 81):
			x = i // 9
			y = i % 9

			if sudoku[x][y] != 0:
				if i == 80:
					return True
				else: 
					continue

			possible_num = possible(x, y)
			for j in possible_num:
				sudoku[x][y] = j
				if backtracking(i + 1):
					return True
				else: # 틀렸을 때, 초기화
					sudoku[x][y] = 0
			return False # 가능한 모든 값을 시도했는데 return 안 되었을 때, False
	else: return True
        
backtracking(0)

for i in range(9):
	for j in range(9):
		print(sudoku[i][j], end=' ')
	print()