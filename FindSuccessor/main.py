# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
       

def inorder(tree):
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
		array.append(tree)
		l.pop(-1)
		tree=tree.right
	return(array)
		
def findSuccessor(tree, node):
    # Write your code here.
	l=inorder(tree)
	for i in range(0,len(l)):
		if(i==len(l)-1):
			return(None)
		if(l[i]==node):
			return(l[i+1])
    return None

