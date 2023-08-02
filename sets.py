# Creating a set of kitchen ware
kitchen_ware_set = {"knives", "tablespoons", "chopsticks", "plates", "cups"}

# Length of the set
print("Length of the kitchen ware set:", len(kitchen_ware_set))

# Data type of the set
print("Data type of the kitchen ware set:", type(kitchen_ware_set))

# Accessing elements in the set
for item in kitchen_ware_set:
    print("kitchen_ware item:", item)

# Adding items to the set
kitchen_ware_set.add("stove")
kitchen_ware_set.add("pans")
print("Updated furniture set:", kitchen_ware_set)

# Creating another set
additional_set = {"cooker", "microwave"}

# Combining two sets (Union)
combined_set = kitchen_ware_set.union(additional_set)
print("Combined set:", combined_set)
