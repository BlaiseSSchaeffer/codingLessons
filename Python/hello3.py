# This is an example of defining a function in python
# that has a parameter. We give set the parameter name to name.
# 
# This function simply returns the string "Hello, <name>!"
def hello1(name):
	return "Hello," + name + "!"

# In order to call this function correctly we must pass in a value
# for name. In this case "Brent". So the function will return
# "Hello, Brent!" when it is called.
myStr = hello1("Brent")
print(myStr)

# Printing a newline to sepatate the output
print("\n")

# There is a way to give tha parameter a default value. Simple
# set the parameter equal to default value as demonstrated below.
def hello2(name = "Blaise"):
	return "Hello," + name + "!"

# Now we can call the function with a person's name as the parameter that
# we want to say hello to, or can run the function with no parameters and see
# the default value.
print(hello2("Brent"))
print(hello2())


# Expected output:
# ================
# $ python hello3.py
# Hello, Brent!
#
#
# Hello, Brent!
# Hello, Blaise!


# Notice, if we try to call hello1  without any arguments (parameters),
# then we will get an error... It must be called with an argument passed in
# for name like so: hello1("Brent") 
#
# However, in the case of hello2, we can either call it with no arguments, 
# retutning the defaultm or pass in an argument to sat hello to the person
# of our choosing like so: hello2() or hello2("Brent")