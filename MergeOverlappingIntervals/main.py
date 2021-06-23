def mergeOverlappingIntervals(intervals):
    # Write your code here.
	i=0
	if(len(intervals)==1 or len(intervals)==0):
		return(intervals)
	intervals.sort()
	print(intervals)
	intervals.append("a")
    while( intervals[i+1]!="a" and i<len(intervals)-1):
		if(intervals[i+1][0]<=intervals[i][1]):
			if(intervals[i+1][1]>=intervals[i][1]):
				intervals[i][1]=intervals[i+1][1]
				intervals.pop(i+1)
			    i-=1
			else:
				intervals.pop(i+1)
			    i-=1
		i+=1
	return(intervals[:-1])
