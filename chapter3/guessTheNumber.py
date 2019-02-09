import random

def guess():
	number = random.randint(1, 20)
	attempt = 0
	while (attempt !=  number):
		print('Take a guess')
		attempt = int(input())

		if (attempt < number):
			print('Too low.')
		elif (attempt > number):
			print('Too high.')
		else:
			break
	print('Good job.')

print('I am thinking of a number between 1 and 20.')
guess()

