def suffixMax(arr):
	suffix_max = []
	suffix_max.append(max(arr[0],0))
	for i in range(1, len(arr)):
		suffix_max.append(max(suffix_max[i-1] + arr[i],0))
	
	return suffix_max


def subarrayMax(arr):
	suffix_max = suffixMax(arr)
	print("Suffix Array:\n",suffix_max)

	max_sum, from_ind, to_ind = 0, 0, 0

	for i in range(len(arr)):
		max_sum = max(max_sum, suffix_max[i])
		if(suffix_max[i] == 0):
			from_ind = i

		if(suffix_max[i] == max_sum):
			to_ind = i
		
	return from_ind, to_ind, max_sum
	


def main():
	print("\n\t\tMaximal Sub-Array Sum Finder")
	print("Enter a List of Numbers: ")
	arr = list(map(int, input().split()))
	print("Array:\n",arr)	
	
	i, j, max_sum = subarrayMax(arr)
	if(i>=j):	#excluding impossible combinations
		i, j = 0, 0
	
	print("\ni : {0}\tj : {1}\nMaximal Subarray Sum: {2}".format(i,j,max_sum))

def timeTester():
	import random
	import matplotlib.pyplot as plt
	import time

	times = []
	n_values = []

	for n in range(10, 1000, 50):
		res = [random.randrange(1000) for i in range(n)]
		start = time.time()
		max_sum = subarrayMax(res) #function to test
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