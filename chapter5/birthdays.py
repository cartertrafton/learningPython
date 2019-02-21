# this program is an intro to dictionaries in python. 
# it prompts the user for a name 
# checks that name in a dictionary and 
# prints the birthday or
# asks the user for the birthday if the name is unrecognized

birthdays = {'Aly': 'Dec 20', 'Tia':'Feb 16', 'Willow':'Feb 20'}
while True:
	print('Enter a name: (blank to quit)')
	name = input()
	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else: 
		print('I do not have birthday information for ' + name)
		print('What is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('Birthday database updated.')
