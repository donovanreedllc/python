# LinkedIn Learning Python course by Joe Marini
# Example file for using built-in functions
#

mystring = "The quick, brown fox jumped over the lazy dog!"
my_numbers = [1,3,5,6,9,12,14,17,20,30]

# the len() function calculates the length of a sequence
# print(len(mystring))

# the max() and min() functions will find the largest and smallest value in a sequence
# print(max(my_numbers))
# print(min(my_numbers))

# the str() function will return a string version of an object
# prefix = "result: "
# result = 5

# print(prefix + str(5))

# minor change to test push to github

# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops 
print(range(1, 10, 3))

# the print function itself is pretty flexible - you can embed variables directly in it
greeting = "Hello"
count = 10
name = "Luffy"

print(f"{greeting} {name} you are customer number {count}")
