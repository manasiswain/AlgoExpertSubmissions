def ola(array,a,j):
	if(array[a-1]>array[a]):
		for i in range(a,len(array)):
			if(j<array[i]):
				return False
			j=array[i]
		return True
	else:
		for i in range(a,len(array)):
			if(j>array[i]):
				return False
			j=array[i]
		return True
def isMonotonic(array):
    # Write your code here.''
	if(len(array)>2):
		j=array[1]
		if(array[0]==array[1]):
			i=2
			while(i!=len(array)):
				if(j>array[i] or j<array[i]):
					boo=ola(array,i,j)
			        return(boo)
				j=array[i]
				i+=1
			return True
		else:
			if(array[0]>array[1]):
				for i in range(2,len(array)):
					if(j<array[i]):
						return(False)
					j=array[i]
				return(True)
			else:
				for i in range(2,len(array)):
					if(j>array[i]):
						return(False)
					j=array[i]
				return(True)
	else:
		return(True)


