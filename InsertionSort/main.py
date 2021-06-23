def insertionSort(array):
    # Write your code here.
	for i in range(1,len(array)):
		s=0
		j=i-1
		key=array[i]
		while(j>=0 and array[j]>key):
			array[j + 1]=array[j]
            j=j-1
		array[j + 1] = key;
	return(array)
			
    pass

