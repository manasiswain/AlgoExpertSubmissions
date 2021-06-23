import itertools
  
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
def kadanesAlgorithm(array):
    # Write your code here.
	l=[]
	max=array[0]
	for i in range(0,len(array)):
		k=i+1
		while(k<=len(array)):
			sum=0
			for j in range(i,k):
				sum+=array[j]
		    l.append(sum)
			if(sum>max):
				max=sum
			k+=1
	print(max)
	print(l)
	return(max)		
		
    pass
