def spiralTraverse(array):
    # Write your code here.00 01 02 03 13 23 33 32 31 30 20 10 11 12 22 21
	l=[]
	#
	d=0
	for i in array:
		for j in i:
			d+=1
	for i in range(0,len(array)):
		if(len(l)==d):
			break
		for j in range(i,len(array[i])-i):
			l.append(array[i][j])
		if(len(l)==d):
			break
		for k in range(i+1,len(array)-i):
			l.append(array[k][-i-1])
		if(len(l)==d):
			break
		p=len(array[-i-1])-i-2
		while(p>=i):
			l.append(array[-i-1][p])
			p-=1
		if(len(l)==d):
			break
		k=len(array)-i-2
		while(k>=i+1):
			l.append(array[k][i])
			k-=1
	print(l)
	return(l)
   
	
	
	
	
