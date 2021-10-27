## Title: 잃어버린 괄호
## Number: 1541
## Date: 2021.10.27

line = input().split('-')

result = 0
for i in range(len(line)):
	num = sum(list(map(int, line[i].split('+'))))
	if i == 0: result += num
	else: result -= num

print(result)