amicable = {}

def devider(n):
	sum = 0
	for i in range(1, n):
		if n % i == 0: sum += i
	return sum

answer = 0
for number in range(1, 10000 + 1):
	a = devider(number)
	if a != number and number == devider(a): answer += number

print answer
