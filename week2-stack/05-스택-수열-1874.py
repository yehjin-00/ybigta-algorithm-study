## Title: 스택 수열
## Number: 1874
## Date: 2021.10.05

num = int(input())

target = []
for i in range(num): 
	target.append(int(input()))

input_num = list(range(num, 0, -1))

complete = True
stack = []
result = []
m = 0

while complete and m < num:
	if len(stack) == 0: 
		stack.append(input_num.pop())
		result.append('+')
	elif target[m] < stack[-1]: complete = False
	elif target[m] > stack[-1]: 
		stack.append(input_num.pop())
		result.append('+')
	else:
		stack.pop()
		result.append('-')
		m += 1		

if complete and len(stack) == 0: 
	for r in result: 
		print(r)
else: print('NO')