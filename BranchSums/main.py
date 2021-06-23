
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def calc(root,sum,l):
    # Write your code here.
	if(root!=None):
		sum+=root.value
		if(root.left==None and root.right==None):
			l.append(sum)
		calc(root.left,sum,l)
		calc(root.right,sum,l)
def branchSums(root):
	sum=0
	l=[]
	calc(root,sum,l)
	sum=0
	return(l)
