# This program serves the purpose of demonstrating while loops

# A while loop is basically a for loop that we have a little bit more
# of, at least in my opinion. We initialize a variable that we will use
# keeptrack of where we are in the while loop. we then set a value for how
# many times we want to loop through the code... Notice that i is initialied to 0
# we are computer scientists! IMPORTANT, see how we have to manually increment
# the value of i in our code. If we didn't do this them we would have an infinite
# loop, and the program would run forever, unless we stop it. By the way, to stop
# execution of a program, type "control" + "c". This program simply loops through 
# ten times and prints out the value of i.
i = 0
while i < 10:
    print(i)
    i = i + 1  # There are multipe ways to incremt a value, for example... i = 1 + 1
               # i += 1 and i++  these last two are most common.

print()

# Here is just another simple example.
myList = ["Blaise", "Mackenzie", "Brent"]
i = 0
j = len(myList)
while i < j:
    print(myList[i])
    i += 1

# Expected Output:
# ================
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#
# Blaise
# Mackenzie
# Brent
