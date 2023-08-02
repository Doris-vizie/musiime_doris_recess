# Regular expressions
""" summary
\d: Mathes any digit(0-9)
\w: Mathes any alphanumeric character {a-z, A-Z, 0-9} and underscore
\s: Mathes any whitespace character (space, tab, newline, etc.)
.: Matches any character except a newline
*: Matches zero or more occurrences of the preceding character or group
+: Matches one or more occurrences of the preceding character or group
?: Matches zero or one occurrences of the preceding character or group
[]: Matches any character within the square brackets
[^]: Matches any character not within the square brackets
^: Matches the start of a line
$: Matches the end of a line
"""
# Matching and searching
# regex re.match(), refindall()

""" summary
re.search(pattern, string): Searches for the first occurrence of the pattern in the string
re.findall(pattern, string): Searches for all occurrences of the pattern in the string
re.match(pattern, string): Searches for the first occurrence of the pattern in the string and returns a match object
re.split(pattern, string): Splits the string into substrings based on the pattern
"""
# Example1 Demonstrating regex | Match first word, match group word
import re
text = "hello world"
# Match First word
match = re.search(r"\b\w+\b", text)
if match:
    print("Match: ",match.group())
matches = re.findall(r"\d+", text)
print("Matches: ",matches)

# Example validate email format or email address
# doris.vizie@gmail.com or dorisvizie@gmail.com
import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
email1 = "doris.vizie@gmail.com"
email2 = "doris_vizie@gmailcom"
print(validate_email(email1))
print(validate_email(email2))

 # Generators and Iterators
 # 'yield' 
 # Iterator '__iter__' "__next__" iterator

def factorial(n ):
    for i in range(1, n+1):
        yield i
    return n + 1 

print(list(factorial(5))) 


# return the factorial of a number
""" if n == 0:
return 1
else:
   return n * factorial(n - 1)
# Print the factorial of a number from 1 to 10
for i in range(1,10):
    print(factorial(i)) 
 """
# Generators
def fibonacci():
    a, b = 5, 1
    while True:
        yield a
        a, b = b, a + b
# Print the first 10 fibonacci numbers
for i in range(10):
    print(next(fibonacci())) 

# Iterators
def square():
    for i in range(1,10):
        yield i ** 2
# Create an iterator object that yields the square of numbers from 1 to 10
sq_iterator = square()
# Print the first 5 squares of numbers from 1 to 10
for i in range(5):
    print(next(sq_iterator))  

# Decorators @my_decorator
# Decorators in python allows you to modify the behavior or classes 
#
def my_decorator(func):
    def inner():
            print("This is a decorator")
            func()
    return inner
@my_decorator
def outer():
      print("This is outer decorator")
outer()