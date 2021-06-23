def findClosestValueInBst(tree, target):
    # Write your code here.
	if(tree==None):
		return(None)
	l=[]
	m=[]
	while(tree!=None):
		l.append(tree.value)
		if(target==tree.value):
			return(tree.value)
		if(target>tree.value):
			tree=tree.right
		else:
			tree=tree.left
	for i in l:
		m.append(abs(i-target))
	mi=1000000000
	for i in range(0,len(m)):
		if(mi>m[i]):
			mi=m[i]
			ind=i
	return(l[ind])
	
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

