sqaure_of_sum = 0
sum_of_sqaure  = 0

for i in range(1, 100 + 1):
	sqaure_of_sum += i
	sum_of_sqaure += i ** 2

diff = sqaure_of_sum ** 2 - sum_of_sqaure

print diff
