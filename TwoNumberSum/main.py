def twoNumberSum(array, targetSum):
    # Write your code here.
	for i in range(0,len(array)-1):
		for j in range(i+1,len(array)):
			if(array[i]+array[j]==targetSum):
				return([array[j],array[i]])
	return([])
    pass

