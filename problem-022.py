f = open("names.txt", "r")
lines = f.readlines()
f.close()
lines = lines[0].replace("\n", "").replace("\"", "").split(",")

alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

def worth(word):
	sum = 0
	for alpha in word:
		sum += alphabet.index(alpha) + 1
	return sum

print worth('COLIN')

lines.sort()#key=lambda word: worth(word))

answer = 0
for i, word in enumerate(lines):
	answer += (i + 1) * worth(word)	

print answer
