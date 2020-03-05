def sum(a,i,j):
	total=0
	for k in range(i,j+1):
		total+=a[k]
	return total

def maxsub(a):
	if(max(a)<0):
		print("The maximal subarray is ",a[0:0])
		print("The maximal subarray sum is ",0)
	else:	
		temp=0
		maxsum=-10000
		x=0
		y=0
		for i in range(len(a)):
			for j in range(i+1,len(a)):
				temp=sum(a,i,j)
				if(temp>maxsum):
					maxsum=temp
					x=i
					y=j
		print("The maximal subarray is ",a[x:y+1])
		print("The maximal subarray sum is ",maxsum)			
		print("Start index: ",x)
		print("End index: ",y+1)

a=[]
n=int(input("Enter number of elements in the array "))
for i in range(n):
	x=int(input("Enter the element "))
	a.append(x)
maxsub(a)
		
'''
OUTPUT

185001162@DSL-09:~/Desktop/DAA/a3$ python3 maxsub.py
Enter number of elements in the array 11
Enter the element -2
Enter the element -4
Enter the element 3
Enter the element -1
Enter the element 5
Enter the element 6
Enter the element -7
Enter the element -2
Enter the element 4
Enter the element 3
Enter the element 2
The maximal subarray is  [3, -1, 5, 6]
The maximal subarray sum is  13
Start index:  2
End index:  6
'''
