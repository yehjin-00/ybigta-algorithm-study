## Title: N과 M (2)
## Level: 14_02
## Number: 15650
## Date: 2021.05.12

def combi(lst, save, n):
	if n <= len(lst):
		if n==1:
			for num in lst:
				for value in save:
					print(value, end=' ')
				print(num)     
		else:
			length = len(lst)
			l = lst.copy()
			for num in range(length):
				p = l.pop(0)
				s = save.copy()
				s.append(p)
				combi(l, s, n-1)

n, m = map(int, input().split())

lst = [i+1 for i in range(n)]
save = []
result = []

combi(lst, save, m)