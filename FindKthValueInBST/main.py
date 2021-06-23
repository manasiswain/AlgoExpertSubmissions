# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
	l=[]
	array=[]
	while(1):
		while(tree!=None):
			l.append(tree)
			tree=tree.left
		if(len(l)==0):
			break
		tree=l[-1]
		array.append(tree.value)
		l.pop(-1)
		tree=tree.right
	print(array[-k])
	return(array[-k])
	

