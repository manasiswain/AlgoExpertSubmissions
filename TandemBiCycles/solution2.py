import itertools
def sumi(l):
	sum=0
	for j in l:
		sum+=max(j)
	return(sum)
def tandemBicycle(r,b,fastest):
    # Write your code here.
	all_combinations = []

	list1_permutations = itertools.permutations(r, len(b))

	for each_permutation in list1_permutations:
    	zipped = zip(each_permutation, b)
    	all_combinations.append(list(zipped))
	l=[]

	for i in all_combinations:
		l.append(sumi(i))
	if(fastest==True):
		return(max(l))
	else:
		return(min(l))
    return 0

