# This program uses the pprint library print more pretty

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count)

#	{' ': 13,
#	',': 1,
# 	'.': 1,
#	'A': 1,
#	'I': 1,
#	...
