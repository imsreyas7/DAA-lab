def dcMaxSum(arr, low, high):
    if(low == high):	#base case, only one element
        return arr[0]
    
    else:	#finding maximum of all 3 possible combinations
        mid = (low+high)//2
        return max(	dcMaxSum(arr,low, mid),
					dcMaxSum(arr, mid+1, high),
                    dcMiddleSum(arr, low, mid, high))


def dcMiddleSum(arr, low, mid, high):	#finding the middle sum
	max_sum, left_sum = 0, 0
	for i in range(mid, low-1, -1):	#finding the maximum sum of left subarray
		max_sum = max_sum + arr[i]

		if(max_sum > left_sum):
			left_sum = max_sum

	max_sum, right_sum = 0, 0
	for i in range(mid+1, high):	#finding the maximum sum of right subarray
		max_sum = max_sum + arr[i]

		if(max_sum > right_sum):
			right_sum = max_sum
	
	return left_sum + right_sum		#adding the 2 as max sum of the sub array


def main():
	print("\n\t\tMaximal Sub-Array Sum Finder")
	print("Enter a List of Numbers: ")
	arr = list(map(int, input().split()))
	print("Array:\n",arr)	
	
	max_sum = dcMaxSum(arr, 0, len(arr))
	print("\nMaximal Subarray Sum: {0}".format(max_sum))
	
def timeTester():
	import random
	import matplotlib.pyplot as plt
	import time

	times = []
	n_values = []

	for n in range(10, 1000, 50):
		res = [random.randrange(1000) for i in range(n)]
		start = time.time()
		max_sum = dcMaxSum(res, 0, len(res)) #function to test
		end = time.time()

		n_values.append(n)
		times.append(end-start)

	plt.xlabel("Length of N")
	plt.ylabel("Running Time")
	#plt.scatter(n_values,times)
	plt.plot(n_values, times, label = "O(nlogn)")   #graphing
	plt.grid()
	plt.legend()
	plt.show()
	plt.title("Time Complexity Analysis")


timeTester()
main()