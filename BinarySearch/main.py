def binarySearch(array, target):
    # Write your code here.
	l=array
	l.sort()
	if(len(l)==0 or target not in l):
		return -1
	while(len(l)>0):
		if(len(l)==1 and l[0]==target):
			return(array.index(l[0]))
		mid=len(l)//2
		if(target<l[mid]):
			l=l[:mid]
		elif(target>l[mid]):
			l=l[mid+1:]
		else:
			return(array.index(l[mid]))

