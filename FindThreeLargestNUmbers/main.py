def take_second(elem):
    return elem[1]

def findThreeLargestNumbers(array):
    # Write your code here.
	if(len(array)==3):
		array.sort()
		return(array)
	elif(len(array)>3):
		k=[]
		k.append(max(array))
		array.remove(max(array))
		k.append(max(array))
		array.remove(max(array))
		k.append(max(array))
		array.remove(max(array))
		k.sort()
		return(k)
    pass
