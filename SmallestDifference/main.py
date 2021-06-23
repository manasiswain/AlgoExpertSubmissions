def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	s=999999
	for i in arrayOne:
		for j in arrayTwo:
			if(abs(i-j)<s):
				s=abs(i-j)
				a=i
				b=j
	l=[a,b]
	return(l)
    pass

