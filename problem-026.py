longest = 0
answer = 2

for n in range(2, 1000)
	quotients = []
	quotient = 1000

	while 1:
		if quotient in quotients:
			if len(quotients) > longest:
				longest = len(quotients)
				answer = n

			quotient = 1000
		else:
			quotient %= n
			#TODO
