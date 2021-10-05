## Title: 균형 잡힌 세상
## Number: 4949
## Date: 2021.10.05

line = input()
pair = {'(':')', '[':']'}
while line != '.':
	stack = []
	complete = True
	for v in line:
		if v in ('[', '('): stack.append(v)
		elif v not in (']', ')'): continue
		elif len(stack) == 0 or v != pair[stack[-1]]: complete = False
		else: stack.pop()
	if complete and len(stack)==0: print('yes')
	else: print('no')
	line = input()