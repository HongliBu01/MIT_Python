
s = 'tahxkcbnnspgzienzhzal'

count = 0
maxcount = 0
word_index

for chart in range(len(s)):
	if s[chart - 1] <= s[chart]:
		count += 1
		if maxcount < count:
			maxcount = count
			word_index = chart
	else :
		count = 0

startpos = word_index - maxcount
print("Longest substring in alphabetical order is: ", s[startpos:word_index + 1])