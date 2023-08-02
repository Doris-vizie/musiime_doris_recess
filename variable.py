# Assigning variables 
name = "Musiime Doris"
crib = "Mengo"
is_female = True
height_cm = 150.5

# Output variable values
print("Name:", name)
print("Stays at:", crib)
print("Is Female:", is_female)
print("Height (in cm):", height_cm)

# reassigning variables
height_m = height_cm / 100

# Updated variable values
print("Height (in meters):", height_m)

# swapping variables
m = 2
n = 4
print("\nBefore swapping: m =", m, "n =", n)
m, n = n, m
print("After swapping: m =", m, "n =", n)

# concatenating variables
first = "Dear"
second = " Client"
message = first + ", " + second + ","
print("\nMessage:", message)

# Variable interpolation
price = 1000
quantity = 5
total_charges = price * quantity
print("Total:", total_charges)

# Variable scope
def my_function():
    local_var = "This is an example of a local variable"
    print("\nHere:", local_var)

my_function()

