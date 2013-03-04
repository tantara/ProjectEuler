sum = 0

def cal(number):
	sum = 0
	for digit in number:
		if digit == "1": sum += len("one")
		elif digit == "2": sum += len("two")
		elif digit == "3": sum += len("three")
		elif digit == "4": sum += len("four")
		elif digit == "5": sum += len("five")
		elif digit == "6": sum += len("six")
		elif digit == "7": sum += len("seven")
		elif digit == "8": sum += len("eight")
		elif digit == "9": sum += len("nine")

	if len(number) >= 2:
		if len(number) != 2 and number[-2:] != "00": sum += len("and")
		if number[-2:] == "10": sum += len("ten") - len("one")
		elif number[-2:] == "11": sum += len("eleven") - len("one") - len("one")
		elif number[-2:] == "12": sum += len("twelve") - len("one") - len("two")
		elif number[-2:] == "13": sum += len("thirteen") - len("one") - len("three")
		elif number[-2:] == "14": sum += len("fourteen") - len("one") - len("four")
		elif number[-2:] == "15": sum += len("fifteen") - len("one") - len("five")
		elif number[-2:] == "16": sum += len("sixteen") - len("one") - len("six")
		elif number[-2:] == "17": sum += len("seventeen") - len("one") - len("seven")
		elif number[-2:] == "18": sum += len("eighteen") - len("one") - len("eight")
		elif number[-2:] == "19": sum += len("nineteen") - len("one") - len("nine")
		elif number[-2:-1] == "2": sum += len("twenty") - len("two")
		elif number[-2:-1] == "3": sum += len("thirty") - len("three")
		elif number[-2:-1] == "4": sum += len("forty") - len("four")
		elif number[-2:-1] == "5": sum += len("fifty") - len("five")
		elif number[-2:-1] == "6": sum += len("sixty") - len("six")
		elif number[-2:-1] == "7": sum += len("seventy") - len("seven")
		elif number[-2:-1] == "8": sum += len("eighty") - len("eight")
		elif number[-2:-1] == "9": sum += len("ninety") - len("nine")

	if len(number) >= 3 and number[-3:-2] != "0": sum += len("hundred")
	if len(number) >= 4 and number[-4:-3] != "0": sum += len("thousand")

	return sum


for i in range(1, 1000 + 1):
	number = str(i)
	sum += cal(number)

print sum
