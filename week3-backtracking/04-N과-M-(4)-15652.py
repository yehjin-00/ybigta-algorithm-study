## Title: N과 M (4)
## Level: 14_04
## Number: 15652
## Date: 2021.05.12

def combi(lst, save, n):
    if n==1:
        for num in lst:
            for value in save:
                print(value, end=' ')
            print(num)  
    else:
        length = len(lst)
        l = lst.copy()
        for num in range(length):
            s = save.copy()
            s.append(l[0])
            combi(l, s, n-1)
            l.pop(0)

n, m = map(int, input().split())

lst = [i+1 for i in range(n)]
save = []
result = []

combi(lst, save, m)