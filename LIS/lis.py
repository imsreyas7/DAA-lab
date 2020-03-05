from itertools import chain, combinations
def power_set(s):
	return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

#Exhaustive search
def checkAscending(A,n):
	for i in range(1,n):
		if A[i]<A[i-1]:
			return 0
	return 1
	
def lengthES(A,n):
	maxlen=0
	pow_set=list(power_set(A))
	for i in pow_set:
		if checkAscending(i,len(i))==1:
			if len(i)>maxlen:
				maxlen = len(i)
	print(maxlen)
	
lengthES([2,3,4],3)

lengthES([2,4,3,5,1,7,6,9,8],9)

'''
exam@admins-32:~/Desktop$ python3 lis.py
3
5
'''

#Dynamic Programming
def lengthDP(A,n):
	L=[0 for i in range(n)]
	for j in range(n):
		L[j]=1
		for i in range(j):
			if(A[i]<A[j]):
				L[j]=max(L[i]+1,L[j])
	print(max(L))
	
lengthDP([5,1,5,7,2,4,9,8],8)

lengthDP([2,4,3,5,1,7,6,9,8],9)

'''
exam@admins-32:~/Desktop$ python3 lis.py
4
5
'''
	
#A[n] as infinity
import math
def lengthDPmod(A,n):
	A.append(math.inf)
	L=[0 for i in range(n)]
	for j in range(n):
		L[j]=1
		for i in range(j):
			if(A[i]<A[j]):
				L[j]=max(L[i]+1,L[j])
	print(max(L))
	
lengthDPmod([2, 4, 3, 5, 1, 7, 6, 9, 8],9)

'''
exam@admins-32:~/Desktop$ python3 lis.py
5
'''

#
def LengthDPred(A,n):
	L=[0 for i in range(n)]
	P=[-math.inf for i in range(n)]
	for j in range(n):
		L[j]=1
		for i in range(j):
			if(A[i]<A[j]):
				L[j]=max(L[i]+1,L[j])
				if L[j]>1:
					if L[j]==L[i]+1:
						P[j]=i
					else:
						p[j]=j
	print(L)
	print(P)
	
LengthDPred([5,2,8,6,3,6,9,7],8)

'''
exam@admins-32:~/Desktop$ python3 lis.py
3
5
4
5
5
[1, 1, 2, 2, 2, 3, 4, 4]
[-inf, -inf, 1, 1, 1, 4, 5, 5]
'''

def TraceLIS(A,n):
	L,P=LengthDPred(A,n)
	LIS=[0 for i in range(n)]
	
TraceLIS([5,2,8,6,3,6,9,7],8)

