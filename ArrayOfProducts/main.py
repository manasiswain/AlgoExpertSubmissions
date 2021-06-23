def arrayOfProducts(array):
    # Write your code here.
	l=[]
	if(len(array)==1 or len(array)==0):
		return(array)
	for i in range(0,len(array)):
		p=1
		for j in range(0,len(array)):
			if(j!=i):
				p=p*array[j]
		l.append(p)
	return(l)

