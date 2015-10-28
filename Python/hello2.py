# This is an example of defining a function in python. 
# Notice that this function takes no parameters.
# def means that we will be defining a function,
# in this case we are defining the function to be named hello.
# All functions must have the parentheses () regardless of if
# there are any parameters passed into the funtion or not.
# This function simply returns the string "Hello, world!"
def hello():
	return "Hello, world!"

# To call a function all you have to do is type the name that
# that you gave it. There are a few ways in which we can see/get the
# result that this function returns. The first way is to create
# a variable that will be assigned to what the function returns.
# This is seen below, then we can print the variable. By the way, 
# this is creating a global variable with the name myStr. We will 
# discuss variables and their scope in a later lesson.
myStr = hello()
print(myStr)

# The second way is to simply enclose the function in a print statement
print(hello())


# Expected output:
# ================
# $ python hello2.py
# Hello, world!
# Hello, world!