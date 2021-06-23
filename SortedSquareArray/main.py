def sortedSquaredArray(array):
    # Write your code here.
	l=[]
	if(len(array)>0):
		for i in range(0,len(array)):
			l.append(array[i]*array[i])
		l.sort()
		return l
	else:
		return []

