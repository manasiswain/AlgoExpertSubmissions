def firstNonRepeatingCharacter(string):
	l=list(string)
	d={}
	for i in l:
		d[i]=0
	for i in l:
		d[i]+=1
	for i in d:
		if(d[i]==1):
			return l.index(i)
	
	return(-1)

