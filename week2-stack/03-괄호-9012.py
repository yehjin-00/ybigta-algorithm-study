## Title: 괄호
## Number: 9012
## Date: 2021.10.05

num = int(input())

for i in range(num):
	line = input()
	stack = []
	complete = True
	for v in line:
		if v == '(': stack.append(v)
		elif len(stack) == 0: complete = False
		else: stack.pop()
	
	if complete and len(stack) == 0: print('YES')
	else: print('NO')