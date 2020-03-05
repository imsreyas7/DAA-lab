def expo3(x,n):
	if n=0:
		return 1
	else:
		if n%2 ==0:
			return expo3(x,n/2)*expo(x,n/2)
		else:
			return x*expo(x,n-1)

x=int(input("Enter a number whose power has to be found "))
n=int(input("Enter the power "))
print("The result is ",expo3(x,n))