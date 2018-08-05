# Part 1 of the Python Review lab.

def hello_world():
	print ("hello world")

def greet_by_name(name):
	print ("hello" + name)

def encode(x):
	x=x*3953531
	return x

def decode(x):
	x=x/3953531
	print (x)

hello_world()
greet_by_name("gilad")
x = encode(100)
decode(x)