def expo2(x,n):
	res=1
	while n>0:
		res*=x
	return x

x=int(input("Enter the number whose power needs to be found "))
n=int(input("Enter the power "))
print("The result is ",expo2(x,n))