def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	sum=0
	c=0
	for i in range(0,len(queries)):
		if(i!=len(queries)-1):
			sum+=queries[i]
			c+=sum
    return c

