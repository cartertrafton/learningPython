
# Loops


# while Loop

spam = 0
while spam < 5:
	print('Hello, world.')
	spam++


# break
while True:
	print('Please type your name: ')
	name = input()
	if name == 'your name':
		break
print('Thank you')


# continue
while True:
	print('Who are you?')
	name = input()
	if name != 'Joe':
		continue
	print('Hello, Joe. What is the password? (It is a fish.)')
	password = input()
	if password == 'swordfish':
		break
print('Access granted.')


# for Loop

# range(x) = counts 0:x
print('My name is')
for i in range(5):
	print('Jimmy Five Times (' + str(i) + ')')

# range(x, y) = counts x:y
for i in range(12, 16):
	print(i)

# range(x, y, z) = counts x:y incrementing by z
for i in range(0, 10, 2):
	print(i)

# can also work negatively, counting down
for i in range(5, -1, -1):
	print(i)