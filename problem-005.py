list = []
for i in range(21):
	list.append(0)

for i in range(2, 21):
	number = i
	for j in range(2, 21):
		max = 0
		while 1:
			if number % j != 0: break
			else:
				number /= j
				max += 1
		if max > list[j]: list[j] = max

LCM = 1
for i in range(2, 21):
	LCM *= i ** list[i]

print LCM
