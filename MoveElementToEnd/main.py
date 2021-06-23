def moveElementToEnd(array, toMove):
    # Write your code here.
	k=[]
	l=[]
	for i in range(0,len(array)):
		if(array[i]==toMove):
			k.append(array[i])
		else:
			l.append(array[i])
	for j in k:
		l.append(j)
	return(l)
