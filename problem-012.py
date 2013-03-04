import math

def triangle_numbers():
	a = 1
	sum = 0
	while 1:
		yield sum + a
		a, sum = a + 1, sum + a

def num_of_divisors(n):
	cnt = 0
	for i in range(1, int(math.sqrt(n)) + 1):
		if n % i == 0: cnt += 2
	if int(math.sqrt(n)) ** 2 == n: cnt -= 1
	return cnt

for i in triangle_numbers():
	if num_of_divisors(i) > 500:
		answer = i
		break

print answer
