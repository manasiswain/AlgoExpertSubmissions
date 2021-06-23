def isValidSubsequence(array, sequence):
    # Write your code here.
	k=-1
	if(len(sequence)==0):
		return(True)
	for i in range(0,len(sequence)):
		isp=0
		for j in range(0,len(array)):
			if(sequence[i]==array[j]):
				isp=1
				if(j>k):
					k=j
					break
				else:
					if(sequence[i] in array[j+1:]):#using
						continue
					else:
					    return(False)
		if(isp==0):
			return(False)
	return(True)
				
    pass
