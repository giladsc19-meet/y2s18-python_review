# Write your solution for 1.4 here!

def is_prime(x):
	b = True
	for i in range(x-2):
		if (x%(i+2)==0):
			b = False
			break
	if b == True:
		print ("prime")  
	if b == False:
		print ("not prime")  

is_prime(7)	