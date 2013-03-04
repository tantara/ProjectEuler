def fibonacci():
	a = 1
	b = 1
	while 1:
		yield a
		a, b = a + b, a

N = 4000000
sum = 0
for i, fi in enumerate(fibonacci()):
	if fi > N: break
	if fi % 2 == 0: sum += fi

print sum
