# This program uses for loops to iterate through a list, 
# also demonstrates the use of terms like 'not in'

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
name = input()
if name not in myPets:
	print('I do not have a pet named ' + name)
else:
	print(name + ' is my pet')


