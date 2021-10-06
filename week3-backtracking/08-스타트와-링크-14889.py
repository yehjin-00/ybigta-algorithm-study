## Title: 스타트와 링크
## Number: 14889
## Date: 2021.10.06

import sys
import itertools

num = int(sys.stdin.readline())
matrix = []

for line in sys.stdin.readlines():
	matrix.append(list(map(int, line.split())))

def get_combi(i, j, matrix):
	return matrix[i][j]+matrix[j][i]

def get_team_score(team, matrix):
	combi = itertools.combinations(team, 2)
	team_score = 0
	for j in combi:
		team_score += get_combi(j[0], j[1], matrix)
	return team_score

teams = itertools.combinations(range(0, num), num//2)
min_value = total
for team in teams:
	other = set(range(0, num))-set(team)
	team_score = get_team_score(team, matrix)
	other_score = get_team_score(other, matrix)

	if min_value > abs(team_score-other_score):
		min_value = abs(team_score-other_score)

print(min_value)