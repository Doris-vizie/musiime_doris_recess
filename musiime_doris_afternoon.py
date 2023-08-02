#STRINGS
#exercise one: use the len() function to determine the length of the string
s = "Hello"
length = len(s)
print("The length of the string: " + str(length))
#exercise two: use a for loop in a string
for char in s:
    print(char)
#exercise three: slicing in a string
my_string = "Hello, World!"
substring1 = my_string[7:12] # Get a substring using positive indices
print(substring1)  
substring2 = my_string[-6:-1] # Get a substring using negative indices
print(substring2)  
substring3 = my_string[::2] # Get every other character in the string by a difference of 2
print(substring3)  
substring4 = my_string[::-1] # Reverse the string
print(substring4) 


#BOOLEAN
#exercise: use a condition to show how to use booleans
is_raining = True
has_umbrella = False
# Condition using booleans
if is_raining and not has_umbrella:
    print("Stay indoors.")
elif is_raining and has_umbrella:
    print("Enjoy your walk!")
else:
    print("Have a great day!")


#DICT
mydict = {
    "phone": "iphone",
    "iphonemodel": "iphone11",
    "year": 2023
}
#Exercice one: use the values () method to return a list of values for the dictionary
print(mydict.values())
#Exercise two: check if a key exists in the dictionary
#using in operator
if "phone" in mydict:
    print("Key 'phone' exists in the dictionary.")
else:
    print("Key 'phone' does not exist in the dictionary.")
#using dict.get() method
if mydict.get("key2") is not None:
    print("Key 'key2' exists in the dictionary.")
else:
    print("Key 'key2' does not exist in the dictionary.")
#Exercise three: how to change items, how to update
# Update values using the 'update()' method
mydict.update({"phone": "samsung", "year": 2040})
print(mydict)
#Exercise four: how to add items, how to remove items
mydict.pop("phone") #removes the key "phone" with its value 
print(mydict)
mydict.popitem() #delete the item using LIFO method
print(mydict)
mydict.clear() #clears the whole dictionary
print(mydict)
#how to add items
mydict["capture"] = "pixels"
print(mydict)
#Exercise five:how to loop through the dictionary and how to nest the dictionary
for key, value in mydict.items():
    print(key, "->", value)
#how to nest the dictionary
outer_dict = {
    "key1": 10,
    "key2": {
        "nested_key1": 20,
        "nested_key2": 30
    },
    "key3": 40
}
# Accessing nested values
print(outer_dict["key2"]["nested_key1"])
print(outer_dict["key2"]["nested_key2"])    


#NUMBERS
w = 10 #int
r = 3.9 #float
s = 2j #complex
#convert from int to complex
z = complex(w)
print(z)
print(type(z))
#convert from float to complex
y = complex(r)
print(y)
print(type(y))
#convert from int to float
x = float(w)
print(x)
print(type(x))
#convert from complex to float
t = float(s.real)
print(t)
print(type(t))
v = float(s.imag)
print(v)
print(type(v))
