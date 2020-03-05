def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print("\t",matrix[i][j],end=" ")
		print("\n")

a=int(input("Enter the power for power of the matrix "))

m = int( input("enter first matrix rows "));
n = int( input("enter first matrix columns "));

array1=[[0 for j in range  (0 , n)] for i in range (0 , m)]
result=[[0 for j in range  (0 , n)] for i in range (0 , m)]


print ("enter first matrix elements: " )
for i in range(0 , m):
	for j in range(0 , n):
		array1[i][j]=int (input("enter element "))

def mul(array1,array2):
	result2=[[0 for j in range  (0 , n)] for i in range (0 , m)]

	# i will run throgh each row of matrix1
	for i in range(0 , m):
	# j will run through each column of matrix 2
		for j in range(0 , n):
		# k will run throguh each row of matrix 2
			for k in range(0 , m):
				result2[i][j] += array1[i][k] * array2[k][j]
	return result2


result=mul(array1,array1)
for q in range(0,a-2):
	result = mul(result,array1)


print_matrix(result)
