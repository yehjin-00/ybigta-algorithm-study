## Title: 큐
## Number: 10845
## Date: 2021.09.21

# 성공 version
import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
	order = sys.stdin.readline().split()
	if order[0] == "push": queue.append(order[1])

	elif order[0] == "size": print(len(queue))

	elif order[0] == "empty":
		if len(queue) == 0: print(1)
		else: print(0)

	elif len(queue) == 0: print(-1)

	elif order[0] == "pop": print(queue.pop(0))

	elif order[0] == "front": print(queue[0])

	elif order[0] == "back": print(queue[-1])

# 왜 안 되는지 모르겠는 ver
import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
	order = sys.stdin.readline()
	if order[:4] == "push": queue.append(order.split()[1])

	elif order == "size": print(len(queue))
	
	elif order == "empty":
		if len(queue) == 0: print(1)
		else: print(0)

	elif len(queue) == 0: print(-1)

	elif order == "pop": print(queue.pop(0))

	elif order == "front": print(queue[0])

	elif order == "back": print(queue[-1])