sum = 0
last = 2000000

primes = []
for i in range(last):
	primes.append(1)

for i in range(2, last):
	if primes[i] == 0: continue
	else:
		for j in range(last / i + 1):
			if i * j >= last: break
			primes[i * j] = 0
		primes[i] = 1

for i in range(last):
	if primes[i] == 1: sum += i

print sum
