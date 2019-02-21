# this program creates an empty dictionary, 
# then assigns the default value for each new 'character' to 0
# this loops through the message counting the characters

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character]  + 1

print(count)

# {' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i':
# 6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}
