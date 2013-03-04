found = False

for a in range(1, 1000 + 1):
	if found: break
	for b in range(a, 1000 + 1):
		c = 1000 - a - b
		if a ** 2 + b ** 2 == c ** 2:
			abc = a * b * c
			found = True
			break

print abc
