def prefixSum(arr):
	prefix_sum = []

	for i in range(len(arr)):
		if(i == 0):
			prefix_sum.append(arr[i])
		else:
			prefix_sum.append(prefix_sum[i-1] + arr[i])

	return prefix_sum
	

def bfMaximalArrayQuad(arr):
	max_sum, max_i, max_j = 0, 0, 0

	prefix_sum = prefixSum(arr)
	print("Prefix Sum:\n",prefix_sum)

	for i in range(len(arr)):
		for j in range(i, len(arr)):
			cur_sum = max(prefix_sum[j] - prefix_sum[i] + arr[i],0)	
			print(i,j, cur_sum, prefix_sum[j], prefix_sum[i], arr[i])
			if(cur_sum > max_sum):
				max_sum = cur_sum
				max_i, max_j = i,j

	return max_i, max_j+1, max_sum 


def main():
	print("\n\t\tMaximal Sub-Array Sum Finder")
	print("Enter a List of Numbers: ")
	arr = list(map(int, input().split()))
	print("Array: ",arr)	
	
	i, j, ijsum = bfMaximalArrayQuad(arr)
	print("\ni : {0}\nj : {1}\nMaximal Subarray Sum: {2}".format(i,j,ijsum))
	if(ijsum!=0):
		print("\nSubarray : Array[{0}:{1}]\n".format(i,j),arr[i:j])

def timeTester():
	import random
	import matplotlib.pyplot as plt
	import time

	times = []
	n_values = []

	for n in range(10, 1000, 50):
		res = [random.randrange(1000) for i in range(n)]
		start = time.time()
		max_sum = bfMaximalArrayQuad(res) #function to test
		end = time.time()

		n_values.append(n)
		times.append(end-start)

	plt.xlabel("Length of N")
	plt.ylabel("Running Time")
	plt.plot(n_values, times, label = "O(nlogn)")   #graphing
	plt.grid()
	plt.legend()
	plt.show()
	plt.title("Time Complexity Analysis")


main()
timeTester()