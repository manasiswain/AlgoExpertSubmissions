def isPalindrome(string):
    # Write your code here.
	l=len(string)//2
	if(len(string)%2==0):
		for i in range(0,l-1):
			if(string[i]!=string[-1-i]):
				return(False)
		if(string[l-1]==string[l]):
			return(True)
		else:
			return(False)
	else:
		for i in range(0,l):
			if(string[i]!=string[-1-i]):
				return(False)
		return(True)
    pass

