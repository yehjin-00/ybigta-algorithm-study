## Title: 큐2
## Number: 18258
## Date: 2021.09.22

import sys

n = int(sys.stdin.readline())
start = 0
size = 0
queue = []

for i in range(n):
	order = sys.stdin.readline().split()
	if order[0] == "push": 
		queue.append(order[1])
		size += 1

	elif order[0] == "size": print(size)

	elif order[0] == "empty":
		if size == 0: print(1)
		else: print(0)

	elif size == 0: print(-1)

	elif order[0] == "pop": 
		print(queue[start])
		start += 1
		size -= 1

	elif order[0] == "front": print(queue[start])

	elif order[0] == "back": print(queue[-1])


# deque ver
import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque([])

for i in range(n):
	order = sys.stdin.readline().split()
	if order[0] == "push": deq.append(order[1])

	elif order[0] == "size": print(len(deq))

	elif order[0] == "empty":
		if len(deq) == 0: print(1)
		else: print(0)

	elif len(deq) == 0: print(-1)

	elif order[0] == "pop": print(deq.popleft())

	elif order[0] == "front": print(deq[0])

	elif order[0] == "back": print(deq[-1])

"""
deque
- queue + stack 이라고 생각하면 된다.
- python 에서는 from collections import deque 를 통해서 사용할 수 있다.

deque method
- deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
- deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
- deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
- deque.remove(item): item을 데크에서 찾아 삭제한다.
- deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
"""