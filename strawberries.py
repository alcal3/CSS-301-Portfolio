###aleks calderon
###4.22.19
#adds strawberries into a list and adds 25 more into the quanity of strawberries

def add_fruit(inventory, fruit, quantity):
    if fruit not in inventory: 
        inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity
        
new_inventory = {}

add_fruit(new_inventory, 'strawberries', 10)
print(new_inventory)
add_fruit(new_inventory, 'strawberries', 25)

print(new_inventory)
