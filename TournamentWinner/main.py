def tournamentWinner(competitions, results):
    # Write your code here.
	d={}
	c=0
	l=[]
	if(len(competitions)==0):
		 return ""
	for i in competitions:
		for j in i:
			l.append(j)
	for i in l:
		d[i]=0
	l=list(set(l))
	while(c<len(results)):
		if(results[c]==1):
			d[competitions[c][0]]+=3
		else:
			d[competitions[c][1]]+=3
		c+=1
	m=-1
	for i in l:
		if(d[i]>m):
			v=i
			m=d[i]
		
    return v

