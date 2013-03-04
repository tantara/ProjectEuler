import math

items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 1000000 - 1

cnt = 0
while 1:
	s = len(items) - 1
	if i == 0:
		print items[cnt]
		items.pop(cnt)
		print items
		break
	if i >= math.factorial(s):
		i -= math.factorial(s)
		cnt += 1
	else:
		print items[cnt]
		items.pop(cnt)
		cnt = 0
