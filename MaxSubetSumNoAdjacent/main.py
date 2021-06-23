import itertools
  
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
def adjacent(a,array):	
	t=0
	for i in range(0,len(a)-1):
		for j in range(0,len(array)):
			if(array[j]==a[i]):
				t=j
				break
		if(a[i+1]==array[t+1]):
			return(False)
	return(True)
		
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
	l=[]
	i=1
	b=[]
	if(len(array)==1):
		return(array[0])
	if(len(array)%2==0):
		s=len(array)//2
	else:
		s=(len(array)//2)+1
	l.extend(findsubsets(array, s))
	print(l)
	for i in l:
		if(adjacent(i,array)==True):
			print(i)
			sum=0
			for k in i:
				sum+=k
			b.append(sum)
	for i in array:
		if(max(b)<i):
			return(i)
	return(max(b))
    pass

