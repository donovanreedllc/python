# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0
j = 0

days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]

# define a while loop
# while x < 5:
#     print(x)
#     x += 1
    
# answer = input("Should I stop twin?")
# while answer != "yes":
#   print (answer)
#   answer = input("Should I stop now twin?")

# define a for loop
# for i in range(10) :
#   print(i)
# use a for loop over a collection
leaders = ["Rocks", "Ace", "Luffy"]

#while j < 3:
#  print(leaders(j))

# use the break and continue statements
# for d in days:
#   if d == "thurs":
#       continue
#   print(d)

# using the enumerate() function to get an index and an item
for i,d in enumerate(leaders):
  print(i, d)