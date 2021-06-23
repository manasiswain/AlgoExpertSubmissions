def longestPeak(array):
    # Write your code here.
	isp=0
	i=0
	l=[]
	while(i<len(array)-1):
		if(array[i]<array[i+1]):
			isp=1
			a=i
			b=i+1
			break
		i+=1
	if(isp==0):
		return(0)
	else:
		isp=2
		ct=2
		ina=0
		for i in range(b,len(array)-1):
			if(array[i]==array[i+1]):
				if(ina==1 and isp==2):
					l.append(ct)
					ct=0
					ina=0
				ct=0
				isp=1
			elif(array[i]<array[i+1]):
				isp=2
				if(ina==1):
					l.append(ct)
					ct=0
					ina=0
				if(ct==0):
					ct=2
				else:
				    ct+=1
			else:
				if(isp==2):
					ina=1
					if(ct==0):
						ct=2
					else:
				   	    ct+=1
					if(i+1==len(array)-1):
						l.append(ct)
						break
				else:
					ct=0
		print(l)
		if(len(l)==0):
			return(0)
		return(max(l))

