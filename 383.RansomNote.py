ransomNote ="a"
magazine = "b"
i = 0
T = 0
if len(ransomNote) <= len(magazine):
	for i in range(len(ransomNote)):
		if ransomNote.count(ransomNote[i]) <= magazine.count(ransomNote[i]):
			T = T + 1
	if T == len(ransomNote):
		print('true')
		print(T)
	else:
		print('false')
		print(T)
else:
	print('false')