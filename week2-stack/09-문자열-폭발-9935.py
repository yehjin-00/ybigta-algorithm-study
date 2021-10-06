## Title: 문자열 폭발
## Number: 9935
## Date: 2021.10.06


# 쉬운 방법 but 시간초과
line = input()
bomb = input()
last = len(line)

while last != len(line):
	last = len(line)
	line = ''.join(line.split(bomb))

if len(line) == 0: print('FRULA')
else: print(line)


# stack 사용
line = input()
bomb = input()
size = len(bomb)

stack = []

for c in line:
	stack.append(c)

	if len(stack) >= size:
		blow = True
		for i in range(size):
			if stack[-1-i] != bomb[-1-i]: 
				blow = False
		if blow:
			for i in range(size): stack.pop()

if stack: print(stack.pop(), end='')
else: print('FRULA')
