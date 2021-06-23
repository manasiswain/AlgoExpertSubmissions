def runLengthEncoding(string):
    # Write your code here.
	d={}
	l=[]
	l.append(string[0])
	if(len(string)>0):
		for i in string:
			d[i]=0
		s=""
		for i in range(0,len(string)):
			if(string[i] not in l):
				print(d)
				l=[]
				l.append(string[i])
				if(d[string[i-1]]<10):
					s+=str(d[string[i-1]])+str(string[i-1])
					d[string[i-1]]=0
				else:
					while(d[string[i-1]]>10):
						s+='9'+str(string[i-1])
						d[string[i-1]]=d[string[i-1]]-9
					s+=str(d[string[i-1]])+str(string[i-1])
					d[string[i-1]]=0
				d[string[i]]+=1
			else:
				d[string[i]]+=1
		if(d[l[0]]<10):
					s+=str(d[l[0]])+str(l[0])
					d[l[0]]=0
		else:
			while(d[l[0]]>=10):
				s+='9'+str(l[0])
				d[l[0]]=d[l[0]]-9
			s+=str(d[l[0]])+str(l[0])
		
		
		print(s)
		return(s)
			


