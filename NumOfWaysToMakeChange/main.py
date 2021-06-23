def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	l=[]
	k=[]
	for i in range(0,n+1):
		l.append(0)
	l[0]=1
	if(n==0):
		return(1)
	denoms.sort()
	for i in range(0,len(denoms)):
		for j in range(0,n+1):
			if(denoms[i]<=j):
				l[j]=l[j]+l[j-denoms[i]]
				
				if(j==n):
					print(l[j])
					k.append(l[j]) #for not possible
				
	
	print(l)
	isp=0

	for i in k:
		if(i!=0):
			isp=1
	if(isp==0):
		return(0)
	else:
		return(l[-1])
