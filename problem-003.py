N = 600851475143

max = 2

def range(start):
	i = start
	while 1:
		yield i
		i += 1

while 1:
	if N < 2: break;
	else:
		for i in range(max):
			if N % i == 0:
				max = i
				N /= i
				break

print max
