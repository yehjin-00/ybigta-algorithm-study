## Title: 오큰수
## Number: 17298
## Date: 2021.10.05

# 시간 초과
num = int(input())
lst = list(map(int, input().split()))
lst.reverse()
stack = []

for i in range(len(lst)):
	if len(stack) == 0: 
		stack.insert(0, lst[i])
	elif lst[i] > stack[0]:
		stack.insert(0, lst[i])
	else:
		stack.insert(0, stack[0])

for value in stack:
	print(value, end=' ')


# 재도전
num = int(input())
lst = list(map(int, input().split()))
stack = []
pointer = 0
size = 0
result = [0 for i in range(num)]
for i in range(1, num):
	if lst[i] <= lst[i-1]:
		stack.append(i-1)
		size += 1
	else:
		while size > 0 and lst[stack[pointer]] < lst[i]:
			result[stack[pointer]] = lst[i]
			pointer += 1
			size -= 1
		result[i-1] = lst[i]
	result[-1] = -1

while size > 0:
	result[stack[pointer]] = -1
	pointer += 1
	size -= 1

print(' '.join(list(map(str, result))))


import sys
num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for i in range(num)]
for i in range(1, num):
	if lst[i] <= lst[i-1]:
		stack.insert(0, i-1)
	else:
		while len(stack) > 0 and lst[stack[0]] < lst[i]:
			result[stack[0]] = lst[i]
			stack = stack[1:]
		result[i-1] = lst[i]

for v in result:
	print(v, end=' ')
print(' '.join(list(map(str, result))))



# 나의 최선
num = int(input())
lst = list(map(int, input().split()))
stack = []
result = [-1 for i in range(num)]
for i in range(1, num):
	if lst[i] <= lst[i-1]:
		stack.insert(0, i-1)
	else:
		while len(stack) > 0 and lst[stack[0]] < lst[i]:
			result[stack.pop(0)] = lst[i]
		result[i-1] = lst[i]

print(' '.join(list(map(str, result))))




# 나의 최선
num = int(input())
lst = list(map(int, input().split()))
stack = []
result = [-1 for i in range(num)]
for i in range(1, num):
	if lst[i] <= lst[i-1]:
		stack.append(i-1)
	else:
		while len(stack) > 0 and lst[stack[-1]] < lst[i]:
			result[stack.pop()] = lst[i]
		result[i-1] = lst[i]

print(' '.join(list(map(str, result))))







# 결과..
num = int(input())
lst = list(map(int, input().split()))
stack = []
result = [-1 for i in range(num)]
for i in range(num):
	while len(stack) > 0 and lst[stack[-1]] < lst[i]:
		result[stack.pop()] = lst[i]
	stack.append(i)

print(*result)





# 설마..
num = int(input())
lst = list(map(int, input().split()))
stack = []
result = [-1 for i in range(num)]
for i in range(num):
	while len(stack) > 0 and lst[stack[-1]] < lst[i]:
		result[stack.pop()] = lst[i]
	stack.append(i)

print(*result)




