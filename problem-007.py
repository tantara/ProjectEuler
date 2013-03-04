primes = []
cnt = 10001

number = 2
while 1:
	if len(primes) == cnt:
		break
	else:
		isprime = True
		for i in range(len(primes)):
			if number % primes[i] == 0:
				isprime = False
				break
		if isprime: primes.append(number)
		number += 1

print primes[cnt - 1]
