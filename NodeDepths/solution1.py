def nodeDepths(root):
    # Write your code here.
	calc(self,root)
	s=0
	for i in self.l:
		s+=i
	return(s)
    pass

def calc(self,root):
    # Write your code here.
	if(root!=None):
		(self.sum)+=1
		calc(self,root.left)
		calc(self,root.right)
	else:
		(self.l).append(self.sum)
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
		self.sum=0
		self.l=[]
        self.value = value
        self.left = None
        self.right = None
	

