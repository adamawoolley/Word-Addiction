from wordlist import words

addiction = int(input('What is your "Word Addiction" number: '))
addiction_resaults = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for word in words:
	number = 0
	for char in word:
		try:
			number += alphabet.index(char) + 1
		except ValueError:
			pass
	if number == addiction:
		addiction_resaults.append(word)

print(addiction_resaults)

