def check(i,j,matrix):
	isp=0
	if(j==0):
		isp=1
		if(matrix[i][j+1]>0):
			return(True)
	elif(j==len(matrix[i])-1):
		isp=1
		if(matrix[i][j-1]>0):
			return(True)
	if(isp==1):
		if(i==0):
			if(matrix[i+1][j]>0):
				return(True)
			else:
				return(False)
		elif(i==len(matrix)-1):
			if(matrix[i-1][j]>0):
				return(True)
			else:
				return(False)
		else:
			if(matrix[i+1][j]>0 or matrix[i-1][j]>0):
				return(True)
			else:
				return(False)
	else:
		if((matrix[i][j+1])>0):
			return(True)
		elif((matrix[i][j-1])>0):
			return(True)
		if(i==0):
			if(matrix[i+1][j]>0):
				return(True)
			else:
				return(False)
		elif(i==len(matrix)-1):
			if(matrix[i-1][j]>0):
				return(True)
			else:
				return(False)
		else:
			if(matrix[i+1][j]>0 or matrix[i-1][j]>0 ):
				return(True)
			else:
				return(False)
	
def minimumPassesOfMatrix(matrix):
    # Write your code here.
	if(len(matrix)==0):
		return(-1)
	if(len(matrix)==1):
		if((len(matrix[0])==1 and matrix[0][0]<0)or len(matrix[0])==0):
			return(-1)
		else:
			return(0)
	l=[]
	ct=0
	for i in matrix:
		b=[]
		for j in i:
			b.append(j)
			if(j<0):
				ct+=1
		l.append(b)
	count=0
	while(1):
		if(ct==0):
			return(count)
		isp=0
		for i in range(0,len(matrix)):
			for j in range(0,len(matrix[i])):
				if(matrix[i][j]<0):
					if(check(i,j,matrix)==True):
						isp=1
						l[i][j]*=-1
						ct-=1
		if(isp==0):
			return(-1)
		print(l)
		matrix=[]
		for x in l:
			c=[]
			for j in x:
				c.append(j)
			matrix.append(c)
		count+=1

