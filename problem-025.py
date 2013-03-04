def fibonacci():
	a = 1
	b = 0
	while 1:
		yield a
		a, b = a + b, a

for i, fi in enumerate(fibonacci()):
	if len(str(fi)) == 1000:
		print i + 1
		break
