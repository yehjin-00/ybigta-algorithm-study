## Title: 옥상 정원 꾸미기
## Number: 6198
## Date: 2021.10.06

num = int(input())

lst = []
for i in range(num):
	lst.append(int(input()))

stack = []
result = [v for v in range(num-1, -1, -1)]
for i in range(num):
	while stack and lst[stack[-1]] <= lst[i]:
		temp = stack.pop()
		result[temp] = i-temp-1
	stack.append(i)

print(sum(result))


input
6
10
3
7
4
12
2


5