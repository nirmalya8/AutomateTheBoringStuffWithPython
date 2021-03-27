'''
This is a part of a Fantasy game where the Inventory items
are to be displayed in a certain fashion.

A dictionary where the keys are string values describing
the item in the inventory and the value is an integer value
detailing how many of that item the player has is the inventory.
For example, the dictionary value
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.
'''

def dispInventory(inventory):
    '''
    Displays the inventory:
    {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    As
    Inventory:
    12 arrow
    42 gold coin
    1 rope
    6 torch
    1 dagger
    Total number of items: 62
    '''
    print("Items in the Inventory")
    tot = 0
    for k,v in inventory.items():
        print(str(v)+" "+k)
        tot+=v
    print("There are a total of "+str(tot)+" items in the inventory")

def addToInventory(inventory, addedItems):
    '''
    Items can be added to the inventory using this function.
    The addToInventory() function should return a dictionary that
    represents the updated inventory.
    '''
    for i in addedItems:
        inventory[i] = inventory.get(i,0)+1
    return inventory
        

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
dispInventory(inv)


