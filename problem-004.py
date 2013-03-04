def largest_palindrome():
	max = 1
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			palindrome = i * j
			if str(palindrome) == str(palindrome)[::-1]:
				if palindrome > max:
					max = palindrome
					break
	return max

print largest_palindrome()
