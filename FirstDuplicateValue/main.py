def firstDuplicateValue(array):
    # Write your code here.
	l=[]
	for i in array:
		if(i not in l):
			l.append(i)
		else:
			return(i)
	return(-1)

