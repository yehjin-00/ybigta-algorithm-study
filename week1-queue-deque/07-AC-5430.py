## Title: AC
## Number: 5430
## Date: 2021.09.22

import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
	cmds = sys.stdin.readline().rstrip()
	size = int(sys.stdin.readline().rstrip())
	lst = sys.stdin.readline().rstrip()
	lst = lst[1:-1].split(',')

	start = 0
	end = size
	pointer = True

	if cmds.count('D') > size:
		print('error')
	else:
		for cmd in cmds:
			if cmd == 'R': pointer = not pointer
			elif pointer: 
				start += 1
			else: 
				end -= 1
		lst = lst[start:end]

		if not pointer: lst.reverse()
		print('['+','.join(lst)+']')