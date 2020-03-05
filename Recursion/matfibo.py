def mat_mul(a,b):
	if(len(a[0])!=len(b)):
		print("Invalid input")
		return
	c=[[0 for j in range(len(b[0]))]for i in range(len(a))]
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				c[i][j]+=a[i][k]*b[k][j]
	return c

def mat_power(x,n):
	pdt=[[0 for j in range(len(x[0]))]for i in range(len(x))]
	for i in range(len(x)):
		pdt[i][i]=1
	if n==0:
		return pdt
	elif (n%2)!=0:
		return mat_mul(x,mat_power(x,n-1))
	else:
		return mat_mul(mat_power(x,int(n/2)),mat_power(x,int(n/2)))

def mat_fib(n):
	x=[[0,1],[1,1]]
	f=[[0],[1]]
	Fib=mat_mul(mat_power(x,n-1),f)
	print(Fib[0])

mat_fib(5)