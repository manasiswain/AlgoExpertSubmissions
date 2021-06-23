def inOrderTraverse(tree):
    # Write your code here.
	l=[]
	d={}
	ct=0
	while(1):
		while(tree!=None):
			d[tree.value]=ct
			ct+=1
			l.append(tree)
			prev=tree
			tree=tree.left
		if(len(l)==0):
			break
		tree=l[-1]
		ct=d[tree.value]
		l.pop(-1)
		tree=tree.right
		if(tree!=None):
			ct+=1
	sum=0
	for i in d:
		sum+=d[i]
	return(sum)

def nodeDepths(root):
    # Write your code here.
	s=inOrderTraverse(root)
	return(s)
    pass


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
		self.ct=0
        self.value = value
        self.left = None
        self.right = None

