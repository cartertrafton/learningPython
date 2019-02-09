# Local and Global variables with the same name
def spam():
	eggs = 'spam local'
	print(eggs) # prints 'spam local'

def bacon():
	eggs = 'bacon local'
	print(eggs) # brints 'bacon local'
	spam()
	print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

