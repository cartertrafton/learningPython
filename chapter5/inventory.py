# inventory.py

stuff = {'ten foot pole': 1, 'torch': 3, 'gold': 21, 'sword': 1, 'arrow': 20}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(item_total))


displayInventory(stuff)

###########################
# loop through loot:
#   loop through items:
#		if item==loot
#			item_value++
#		else 
#			add new item, val=1

def addToInventory(inventory, addedItems):
	for loot in addedItems:
		inventory.setdefault(loot, 0)
		inventory[loot]= inventory[loot] + 1
	return inventory

inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
