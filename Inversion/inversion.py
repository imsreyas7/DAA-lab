array=[]

def init(array):
	array=[4,3,1,2,5];

def getInput(array):
	q=int(input("Enter the number of elements : "))
	print("Enter a List of Numbers: ")
	for i in range (q):
		array.append(int(input()))

#Brute force
def disorder(array):
	pairs=0

	for i in range(len(array)):
		elt = array[i]
		for j in range(i+1, len(array)):
			if array[i] > array[j]:
				pairs+=1
    
	return pairs

#D&C
def merge(array,buffarray,left,mid,right):
	i,j,k,pairs=left,mid+1,left,0
	while i<=mid and j<=right:
		if array[i]<=array[j]:
			buffarray[k] = array[i] 
			k += 1
			i += 1
		else:  
			buffarray[k] = array[j] 
			pairs += (mid-i + 1)  #There are mid - i inversions if array[i] > array[j]
			k += 1
			j += 1

	while i<=mid: #remaining elements in left
		buffarray[k] = array[i] 
		k += 1
		i += 1
	
	while j <= right: #remaining elements in right
		buffarray[k] = array[j] 
		k += 1
		j += 1

	for x in range(left, right + 1): #copying sorted subarray into original array
		array[x] = buffarray[x] 
          
	return pairs  

def merge_sort(arr, temp_arr, left, right):
  
	pairs = 0
  
	if left < right:
		mid = (left + right)//2
		#calculating no. of inversions as an extension of merge sorting
		pairs += merge_sort(arr, temp_arr, left, mid)  #inversions in left half
		pairs += merge_sort(arr, temp_arr, mid + 1, right) #inversions in right half
		pairs += merge(arr, temp_arr, left, mid, right) #merge
        
	return pairs   

def main():
	print("Enter an array ")
	getInput(array)

	print("\n\tBrute Force Algorithm\n")
	print("Number of disordered pairs in ",array,"is",disorder(array))


	print("\n\tDivide And Conquer Algorithm\n")
	print("Number of disordered pairs in {0} is {1}.\n".format(array, merge_sort(array, [0 for x in range(len(array))], 0, len(array)-1)))

main()

