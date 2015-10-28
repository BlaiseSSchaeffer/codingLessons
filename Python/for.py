#This program serves the purpose of demonstrating for loops in python

# for loops start with for and are then followed by a local variable for the scope 
# of the for loop. In this case, i. You can then set a range to be iterated
# through. Most programming languages start with 0, python does. So, the first time 
# through the loop i has the value of 0, then 1, then 2. So we generally say that we
# go up to, but so not include the value set in range. By the way str() is used to convert
# something to a string.
for i in range(3):
    print("Hello, world! " + str(i))

# We can basically iterate through aything else we want following a syntax similar 
# to the one below, which iterates through a list/string.
names = ["Blaise", "Mackenzie", "Brent"]
for name in names:
    print(name)

myStr = "Iowa"
for char in myStr:
    print(char)

# We can also set a starting value, an ending value, and what we want the it to be 
# increment by explicitly following a format like that shown below
for i in range (10,21,2):
    print(i)

for x in range (100,0,-10):
    print(x)

# Expected output:
# ================
# $ python for.py
# Hello, world! 0
# Hello, world! 1
# Hello, world! 2
# Blaise
# Mackenzie
# Brent
# I
# o
# w
# a
# 10
# 12
# 14
# 16
# 18
# 20
# 100
# 90
# 80
# 70
# 60
# 50
# 40
# 30
# 20
# 10
