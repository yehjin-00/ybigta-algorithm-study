## Title: N과 M (1)
## Level: 14_01
## Number: 15649
## Date: 2021.05.11

def combi(lst, save, n):
	if n==1:
		for num in lst:
			for value in save:
				print(value, end=' ')
			print(num)     
	else:
		for num in range(len(lst)):
			l = lst.copy()
			p = l.pop(num)
			s = save.copy()
			s.append(p)
			combi(l, s, n-1)

n, m = map(int, input().split()

lst = [i+1 for i in range(n)]
save = []
result = []

combi(lst, save, m)