def expo(x,n):
	if n=0:
		return 1
	else:
		return x*expo(x,n-1)

x=int(input("Enter a number whose power is to be calculated "))
n=int(input("Enter the power "))
print("The result is ",expo(x,n))