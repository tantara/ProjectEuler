N = 1000000

def collatz(n):
	cnt = 1
	while 1:
		if n == 1: break
		elif n % 2 == 0: n = n / 2
		else: n = 3 * n + 1
		cnt += 1
	return cnt

longest = 0
answer = 0
for i in range(1, N):
	length = collatz(i)
	if length > longest:
		longest = length
		answer = i

print answer, longest
