def tandemBicycle(r,b,fastest):
    # Write your code here.
	if(fastest==True):
		l=[]
		for i in range(0,len(r)):
			l.append(r[i])
			l.append(b[i])
		while(len(l)>len(r)):
			l.remove(min(l))
		sum=0
		for i in l:
			sum+=i
		return sum
	else:
		r.sort()
		b.sort()
		sum=0
		for i in range(0,len(r)):
			if(r[i]>=b[i]):
				sum+=r[i]
			else:
				sum+=b[i]
		return(sum)

	
    

