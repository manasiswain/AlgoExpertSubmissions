def validStartingCity(distances, fuel, mpg):
    # Write your code here.
	for i in range(0,len(distances)):
		nfuel=0
		isp=1
		for j in range(i,len(distances)+i):
			nfuel+=fuel[j%len(distances)]*mpg
			if(nfuel>=distances[j%len(distances)]):
				nfuel-=distances[j%len(distances)]
			else:
				isp=0
				break
		if(isp==1):
			return(i)
    return -1

