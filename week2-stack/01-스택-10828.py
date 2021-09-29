## Title: 스택
## Number: 10828
## Date: 2021.09.30

import sys
n = int(input())

stack = list()
size = 0
for cmd in sys.stdin.readlines():
	cmd = cmd.split()
	if cmd[0] == 'push':
		stack.insert(size, cmd[1])
		size += 1
	elif cmd[0] == 'size':
		print(size)
	elif cmd[0] == 'empty':
		if size == 0: print(1)
		else: print(0)
	elif size == 0: print(-1)
	elif cmd[0] == 'pop':
		print(stack[size-1])
		size -= 1
	elif cmd[0] == 'top':
		print(stack[size-1])