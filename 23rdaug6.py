# String = player's name
player_name = "Alice"

# List = basket of items
inventory = ["sword", "shield", "potion"]

# Tuple = fixed position (x, y)
position = (5, 9)

# Show game info
print("Welcome,", player_name)   # using string
print("Your items are:", inventory)  # using list
print("You are at position:", position)  # using tuple

# Add a new item to the list (inventory can change)
inventory.append("magic ring")
print("You found a new item! Inventory now:", inventory)

# Tuple cannot change (position is fixed)
# position[0] = 10  <-- this would give error
