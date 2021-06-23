def bubbleSort(array):
    # Write your code here.
	while(1):
		isp=0
		for i in range(0,len(array)-1):
			if(array[i]>array[i+1]):
				isp=1
				temp=array[i]
				array[i]=array[i+1]
				array[i+1]=temp
		if(isp==0):
			return(array)
    pass

