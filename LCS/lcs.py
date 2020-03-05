def lcs(a,b,m,n):

  if(m==0 or n==0): #empty array
    return 0
  elif(a[m-1]==b[n-1]):
    return 1+lcs(a,b,m-1,n-1)
  else:
    return max(lcs(a,b,m-1,n),lcs(a,b,m,n-1))

print(lcs([5,2,8,6,3,6,9,7],[4,7,8,6,3,8,5,5],8,8))

'''
exam@admins-32:~/Desktop$ python3 lcs.py
3
'''

def lcsdp(a,b):
  m=len(a)
  n=len(b)
  Lookup= [[-1]*(n+1) for i in range(m+1)]
  for i in range(m+1):
    for j in range(n+1):
      if(i==0 or j==0):
        Lookup[i][j]=0
      elif(a[i-1]==b[j-1]):
        Lookup[i][j]= Lookup[i-1][j-1] +1
      else: #choosing best subsequence in case it doesn't match
        Lookup[i][j]= max(Lookup[i-1][j],Lookup[i][j-1])
  return Lookup #Best possible subsequence returned in Lookup[m][n]
  
print(lcsdp([5,2,8,6,3,6,9,7],[4,7,8,6,3,6,9,5]))

'''
exam@admins-32:~/Desktop$ python3 lcs.py
[[0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 1, 1, 1, 1, 1, 1],
 [0, 0, 0, 1, 2, 2, 2, 2, 2],
 [0, 0, 0, 1, 2, 3, 3, 3, 3],
 [0, 0, 0, 1, 2, 3, 4, 4, 4],
 [0, 0, 0, 1, 2, 3, 4, 5, 5],
 [0, 0, 1, 1, 2, 3, 4, 5, 5]]
 '''
 
def backtrace(a,b):
 Lookup = lcsdp(a,b)
 m,n=len(a),len(b)
 i,j=m,n

 Lcsindex=Lookup[m][n]
 Lcs=""

 while(i>0 and j>0):
   if(a[i-1]==b[j-1]): #appending to sequence in case of matching value
     Lcs=Lcs+str(a[i-1])
     i-=1
     j-=1
   elif(Lookup[i-1][j]>Lookup[i][j-1]): #move the table leftward
     i-=1
   else: #move the table upwards
     j-=1
  
 return Lcs[::-1]
  
print(backtrace([5,2,8,6,3,6,9,7],[4,7,8,6,3,6,9,5]))

'''
exam@admins-32:~/Desktop$ python3 lcs.py
86369
'''
