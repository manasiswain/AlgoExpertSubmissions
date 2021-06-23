def hasSingleCycle(array):
    # Write your code here.
	vis=[]
	for i in range(0,len(array)):
		vis.append(0)
	for i in range(0,len(array)):
		start=i
		j=i
		jump=0
		count=0
		while(count<len(array)):
			if(array[j]==0):
				break
			if(vis[j]==1):
				if(j!=start):
					if(vis[start]==1):
						break
					else:
						count+=1
				else:
					if(0 in vis):
						break
					else:
						return(True)
			if(array[j]<0):
				ct=abs(array[j])
				jj=j
				while(1):
					if(ct==0):
						jump=jj
						break
					if(jj==0):
						jj=len(array)-1
					else:
						jj=jj-1
					ct-=1
			else:
				jump=(j+array[j])%len(array)
			vis[jump]=1
			j=jump
		for k in range(0,len(array)):
			vis[k]=0
			
	return(False)
		
    pass

