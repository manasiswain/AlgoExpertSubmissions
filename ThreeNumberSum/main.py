import itertools
  
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
def threeNumberSum(array, targetSum):
    # Write your code here.
	l=findsubsets(array,3)
	k=[]
	for i in l:
		sum=0
		for j in i:
			sum+=j
		if(sum==targetSum):
			i=list(i)
			i.sort()
			k.append(i)
	k.sort()
	print(k)
	return(k)

