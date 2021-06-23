# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def deep(i,deapth,sum):
	deapth+=1
	for j in i:
		
		if(type(j)==int):
			sum+=j*deapth
		else:
			sum+=(deep(j,deapth,0)*deapth)
	print(sum,deapth)
	return(sum)
def productSum(array):
    # Write your code here.
	deapth=1
	sum=0
	for i in array:
		if(type(i)==int):
			sum+=i*deapth
		else:
			sum+=deep(i,1,0)
			deapth=1
		print("//",sum)
	return(sum)
					
    pass
