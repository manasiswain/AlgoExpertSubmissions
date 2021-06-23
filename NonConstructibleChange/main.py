import itertools
  
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
def findsum(l):
	x=[]
	for i in l:
		sum=0
		for j in i:
			sum+=j
		x.append(sum)
	return(x)

def nonConstructibleChange(coins):
    # Write your code here.
	if(len(coins)>0):
		l=[]
		m=[]
		for i in range(1,len(coins)+1):
			l.extend(findsubsets(coins,i))
		m.extend(findsum(l))
		i=1
		while(1):
			if i not in m:
				return(i)
			i+=1
	else:
		return(1)
	
				
	

