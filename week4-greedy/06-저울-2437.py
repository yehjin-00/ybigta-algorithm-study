## Title: 저울
## Number: 2437
## Date: 2021.10.27

# 1차 시도 (시간 초과)
def make(lst, target):
	if target in lst: return True
	for i in range(len(lst)):
		new_lst = lst[:]
		new_lst.pop(i)
		if make(new_lst, target-lst[i]): return True
	return False

N = int(input())
lst = sorted(list(map(int, input().split())))

for i in range(1, sum(lst)+1):
	if not make(sorted(list(filter(lambda x: x<=i, lst)), reverse=True), i):
		print(i)
		break


# 2차 시도 (시간 초과)
def make(lst, target):
	if target in lst: return True
	if len(lst) < 2: return False
	if make(lst[1:], target-lst[0]): return True
	if make(lst[1:], target): return True
	return False

N = int(input())
lst = sorted(list(map(int, input().split())))

for i in range(1, sum(lst)+1):
	if not make(sorted(list(filter(lambda x: x<=i, lst)), reverse=True), i):
		print(i)
		break

# 3차 시도
def make(lst, target):
	if target in lst: return True
	if len(lst) < 2: return False
	if make(lst[1:], target-lst[0]): return True
	if make(lst[1:], target): return True
	return False

N = int(input())
lst = sorted(list(map(int, input().split())))

check = [False] * (sum(lst)//2 + 1)

for i in range(1, sum(lst)//2 + 1):
	small_lst = sorted(list(filter(lambda x: x<i, lst)), reverse=True)

	if check[i]: continue
	# i가 주어진 숫자이거나 i보다 작은 숫자를 다 더한 것이 i와 같을 때,
	elif i in lst or sum(small_lst)-i == 0: 
		check[i] = True
		check[sum(small_lst)-i] = True
		check[sum(lst)-i] = True
	# i보다 작은 숫자를 다 더한 것이 i보다 작을 때, (불가능)
	elif sum(small_lst) - i < 0: 
		print(i)
		break
	elif sum(small_lst)-i < i:
		check[i] = True
	elif make(small_lst, i): 
		check[i] = True
		check[sum(small_lst)-i] = True
		check[sum(lst)-i] = True
	else:
		print(i)
		break

# 4차 시도
def make(lst, target):
	if target in lst: return True
	if len(lst) < 2: return False
	if make(lst[1:], target-lst[0]): return True
	if make(lst[1:], target): return True
	return False

N = int(input())
lst = sorted(list(map(int, input().split())))

for i in range(1, sum(lst)//2 + 1):
	small_lst = sorted(list(filter(lambda x: x<i, lst)), reverse=True)

	if i in lst:  continue
	elif sum(small_lst)-i >= 0 and sum(small_lst)-i <= i: continue
	elif sum(small_lst) - i < 0: 
		print(i)
		break
	elif not make(small_lst, i): 
		print(i)
		break

# 5차 시도
def make(lst, target):
	if target in lst: return True
	if len(lst) < 2: return False
	if make(lst[1:], target-lst[0]): return True
	if make(lst[1:], target): return True
	return False

N = int(input())
lst = sorted(list(map(int, input().split())))

small = 0
for i in range(len(lst)):
	if lst[i] > 1:
		small = i
		break

for i in range(1, sum(lst)//2 + 1):
	for j in range(small, len(lst)):
		if lst[j] > i:
			small = j
			break

	small_lst = lst[:small]

	if i in lst:  continue
	elif sum(small_lst)-i >= 0 and sum(small_lst)-i <= i: continue
	elif sum(small_lst) - i < 0: 
		print(i)
		break
	elif not make(small_lst, i): 
		print(i)
		break

# 6차 시도
# 인터넷의 도움을 받음,,
# n개의 추로 m까지의 숫자를 만들 수 있다면, k 무게의 추를 추가하면 m+k까지 만들 수 있다.
# 단, k가 m+1보다 커서는 안된다.
N = int(input())
lst = sorted(list(map(int, input().split())))
check = 0
for i in lst:
	if i > check+1:
		break
	else:
		check += i       

print(check+1)
