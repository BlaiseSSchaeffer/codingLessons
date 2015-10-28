# Now we are going to quickly demonstrate how to gather
# input from the user.

def hello(name):
	return "Hello, " + name + "!"

# By using the built in input we can gather information from the command
# line. Asking the user to enter a name, which we can use in our program.
name = input("Enter the name of someone you would like to say hello to: ")

print(hello(name))

# Expected Output:
# ================
# $ python hello4.py
# Enter the name of someone you would like to say hello to: <Enter_a_name>
# Hello, <name_you_entered>!