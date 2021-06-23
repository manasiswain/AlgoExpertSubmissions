def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	l=[]
	k=[]
	for i in range(0,n+1):
		l.append(0)
	if(n==0):
		return(0)
	denoms.sort()
	for i in range(0,len(denoms)):
		for j in range(0,n+1):
			if(denoms[i]<=j):
				x=j-denoms[i]
				if(l[x]==0 and x!=0):
					
					if(j==n):
						print(l[j])
						k.append(l[j])
				else:
					if(i==0):
						l[j]=1+l[x]
					else:
						if(l[j]==0):
							l[j]=1+l[x]
					if(i!=0 and l[j]>=l[x]+1 ):
						l[j]=1+l[x]
					if(j==n):
						print(l[j])
						k.append(l[j]) #for not possible
				
	
	print(l)
	min=999
	isp=0
	for i in k:
		if(i!=0):
			isp=1
			if(min>i):
				min=i
	if(isp==0):
		return(-1)
	else:
		return(min)
