# Similar programming to allMyCats1.py but now utilizes:
# 	- while and for loop
#	- list data structure, instead of mulitple variables
# 	- len() function of lists

catNames = []
while True:
	print()

	name = input('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.): ')
	if name == '':
		break
	catNames = catNames + [name] # List Concatentation
print('The cat names are: ')
for name in catNames:
	print('  ' + name)

