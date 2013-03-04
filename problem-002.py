N=4000000
sum = 0

fi = 0
for i in range(10)
	if i == 1: fi = 1
	elif i == 2: fi = 2
	else: fi = fi + i
	if fi % 2 == 0: sum += fi
	print sum

print sum
