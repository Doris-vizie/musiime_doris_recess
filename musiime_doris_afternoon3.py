#EXERCISE 1(lists)
# 1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ["John", "Alice", "Michael", "Sarah", "David"]
if len(names) >= 2:
    second_item = names[1]
    print("The second item is:", second_item)
else:
    print("The list does not have a second item.")
# 2. Write a python program to change the value of the first item to a new value
names = ["John", "Alice", "Michael", "Sarah", "David"]
names[0] = "Bob"
print("The first item is now:", names[0])
# 3. Write a python program to add a sixth item to the list
names = ["John", "Alice", "Michael", "Sarah", "David"]
names.append("Eric")
print("The list now contains:", names)
# 4. Write a python program to add “Bathel” as the 3rd item in your list
names = ["John", "Alice", "Michael", "Sarah", "David"]
names.insert(2, "Bathel")
print("The list now contains:", names)
# 5. Write a python program to remove the 4th item from the list
names = ["John", "Alice", "Michael", "Sarah", "David"]
names.remove(names[3])
print("The list now contains:", names)
# 6. Use negative indexing to print the last item in your list
names = ["John", "Alice", "Michael", "Sarah", "David"]
last_item = names[-1]
print("The last item is:", last_item)
# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
names = ["John", "Alice", "Michael", "Sarah", "David", "Eric", "Bathel"]
print("The 3rd item is:", names[2])
print("The 4th item is:", names[3])
print("The 5th item is:", names[4])
# 8. Write a list of countries and make a copy of it.
countries = ["France", "Germany", "Italy", "Spain"]
new_countries = countries.copy()
print("The original list is:", countries)
print("The new list is:", new_countries)
# 9. Write a python program to loop through the list of countries
countries = ["France", "Germany", "Italy", "Spain"]
for country in countries:
    print(country)
# 10. Write a list of animal names and sort them in both descending and ascending order
animals = ["dog", "cat", "bird", "fish", "cow", "horse", "pig"]
animals.sort(reverse=True)
print("The animals in descending order are:", animals)
animals.sort()
print("The animals in ascending order are:", animals)
# 11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
animals = ["dog", "cat", "bird", "fish", "cow", "horse", "pig"]
for animal in animals:
    if "a" in animal:
        print(animal)
# 12. Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["John", "Alice", "Michael", "Sarah", "David"]
second_names = ["Bathel", "Eric", "Misach", "Doris", "Anna"]
full_names = first_names + second_names
print("The full names are:", full_names)

#EXERCISE 2(tuples)
# 1. Consider the tuple below;
# x = (“samsung”, “iphone”, “tecno”, “redmi”)
# Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
if len(x) >= 1:
    print("The favorite phone brand is:", x[1])
else:
    print("The list does not have a favorite phone brand.")
# 2. Use negative indexing to print the 2nd last item in your tuple
x = ("samsung", "iphone", "tecno", "redmi")
print("The 2nd last item is:", x[-2])
# 3. Using the phones list above, write a python program to update “iphone” to “itel”
x = ("samsung", "iphone", "tecno", "redmi")
xlist = list(x)
xlist[1] = "itel"
x = tuple(xlist)
print("The list now contains:", x)
# 4. Write a python program to add “Huawei” to your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
xlist = list(x)
xlist.append("Huawei")
x = tuple(xlist)
print("The list now contains:", x)
# 5. Write a python program to loop through the tuple above
x = ("samsung", "iphone", "tecno", "redmi")
for phone in x:
    print(phone)
# 6. Write a python program to remove/delete the first item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
xlist = list(x)
xlist.pop(0)
x = tuple(xlist)
print("The list now contains:", x)
# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu", "Mbale"])
print(cities)
# 8. Write a python program to unpack your tuple.
cities = ('Kampala', 'Entebbe', 'Jinja', 'Gulu', 'Mbale')
city1, city2, city3, city4, city5 = cities
print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)
print("City 4:", city4)
print("City 5:", city5)
# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above
cities = ('Kampala', 'Entebbe', 'Jinja', 'Gulu', 'Mbale')
print("The 2nd city is:", cities[1])
print("The 3rd city is:", cities[2])
print("The 4th city is:", cities[3])
# 10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("Musiime", "Grier")
second_names = ("Doris", "Raphael")
full_names = first_names + second_names
print("The full names are:", full_names)
# 11. Create a tuple of colors and multiply it by 3.
colors = ("red", "green", "blue", "yellow")
print("The colors are:", colors)
print("The colors are:", colors * 3)
# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print("The number of times 8 appears in this tuple is:", thistuple.count(8))

#EXERCISE 3(sets)
# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(("coffee", "tea", "milk"))
print("The beverages are:", beverages)
# 2. Use the correct method to add 2 more items to the beverages set.
beverages = set(("coffee", "tea", "milk"))
beverages.add('Orange Juice') # Using the add() method to add a single item
beverages.update(['Milkshake', 'Iced Tea']) # Using the update() method to add multiple items
print("The beverages are:", beverages)
# 3. Given the set below;
#mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
#Check if microwave is present in the set.
mySet = {"oven","kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")
# 4. Write a python program to remove “kettle” from the set above.
mySet = {"oven","kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print("The beverages are:", mySet)
# 5. Write a python program to loop through the set above.
mySet = {"oven","kettle", "microwave", "refrigerator"}
for kitchenware in mySet:
    print(kitchenware)
# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
my_set = {'apple', 'banana', 'orange', 'grape'}
my_list = ['kiwi', 'pear']
print("Before update:")
print("Set:", my_set)
print("List:", my_list)
my_set.update(my_list)
print("After update:")
print("Set:", my_set)
# 7. Write two sets, one containing your ages and the other your first names. Join the two sets
ages = {25, 30, 35}
names = {'John', 'Alice', 'Michael'}
joined_set = ages.union(names) # Using the union() method
print("Joined set using union():", joined_set)
joined_set = ages | names # Using the | operator
print("Joined set using | operator:", joined_set)

#EXERCISE 4(Strings)
# 1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
my_integer = 42
my_string = "The answer is: "
concatenated_string = my_string + str(my_integer)
print(concatenated_string)
#2. Consider the example below;
#Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
replaced = txt.replace(" ", "")
content = txt.strip()
print(content)
# 3. Write a python program to convert the value of ‘txt’ to uppercase
txt = " Hello, Uganda! "
print(txt.upper())
# 4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt = " Hello, Uganda! "
print(txt.replace('U', 'V'))
# 5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
y = "I am proudly Ugandan"
print(y[2:4])
# 6. The piece of code below will give an error when output;
#Write a python program to correct it.
#x = "All “Data Scientists” are cool!"
x = 'All “Data Scientists” are cool!'
print(x)

#EXERCISE 5(dictionaries)
 # 1. With reference to the dictionary below, write a python program to print the value of the shoe size. 
#Add this dictionary to your .py file
Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}

shoe_size = Shoes["size"]
print("Shoe Size:", shoe_size)
# 2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print(Shoes)
# 3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print(Shoes)
# 4. Write a python program to return a list of all the keys in the dictionary above.
print(Shoes.keys())
#5. Write a python program to return a list of all the values in the dictionary above.
print(Shoes.values())
# 6. Check if the key “size” exists in the dictionary above.
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")
# 7. Write a python program to loop through the dictionary above.
for key, value in Shoes.items():
    print(key, ":", value)
# 8. Write a python program to remove “color” from the dictionary.
Shoes.pop("color")
print(Shoes)
# 9. Write a python program to empty the dictionary above.
Shoes.clear()
print(Shoes)
# 10. Write a dictionary of your choice and make a copy of it.
# Create a dictionary
original_dict = {
    "name": "John",
    "age": 30,
    "country": "USA"
}
copied_dict = original_dict.copy() # Make a copy of the dictionary
original_dict["age"] = 31 # Modify the original dictionary
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)
# 11. Write a python program to show nested dictionaries
nested_dict = {
    "name": "John",
    "age": 30,
    "country": "USA",
    "address": {
        "city": "New York",
        "state": "NY"
    }
}
print("Nested Dictionary:", nested_dict)
print("The city is: " + nested_dict["address"]["city"])