## Title: 후위 표기식
## Number: 1918
## Date: 2021.10.06

line = input()
operator = []

for v in line:
	if v not in ('+', '*', '-', '/', '(', ')'):
		print(v, end='')

	elif v == '(':
		operator.insert(0, v)

	elif v in ('*', '/'):
		while operator and operator[0] in ('*', '/'):
			print(operator.pop(0), end='')
		operator.insert(0, v)

	elif v in ('+', '-'):
		while operator and operator[0] in ('*', '/', '+', '-'):
			print(operator.pop(0), end='')
		operator.insert(0, v)

	elif v == ')':
		while operator and operator[0] in ('*', '/', '+', '-'):
			print(operator.pop(0), end='')
		operator.pop(0)

while operator:
	print(operator.pop(0), end='')