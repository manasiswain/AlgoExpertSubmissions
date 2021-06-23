def classPhotos(r,b):
    # Write your code here.
	r.sort()
	b.sort()
	if(len(r)>=1 and len(b)>=1):
		ct=0
		while(r[ct]==b[ct]):
			return False
		if(r[ct]>=b[ct]):
			for i in range(ct+1,len(r)):
				if(r[i]<=b[i]):
					return False
			return True
				
		elif(b[ct]>=r[ct]):
			for i in range(ct+1,len(r)):
				if(b[i]<=r[i]):
						return False
			return True
			
			
	else:
        return False

