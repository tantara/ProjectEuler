startyear = 1900
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0 # monday(0)-sunday(6)

answer = 0
for year in range(startyear, 2000 + 1):
	for month in range(1, 12 + 1):
		if day == 6 and year != 1900: answer += 1
		if month == 2 and year % 4 == 0 and year % 400 != 0: day += 1
		day = (day + days[month] - 1) % 7

print answer
