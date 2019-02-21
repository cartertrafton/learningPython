# values vs items vs keys in Python3
# exDictionary = { key:value }
# item = ('key', 'value')

spam = {'color': 'red', 'age': 42}

for v in spam.values():
	print(v)	# red
			# 42

for k in spam.keys():
	print(k)	# color
			# age

for i in spam.items():
	print(i)	# ('color', 'red')
			# ('age', 42)


# list() function
list(spam.keys())	# ['color', 'age']
