#This Function has been used in all 4 programs to find running times for the different
#algorithms and the resulting graphs have been saved.

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
	plt.plot(n_values, times, label = "O(nlogn)")   #graphing
	plt.grid()
	plt.legend()
	plt.show()
	plt.title("Time Complexity Analysis")