# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(p):
    # Write your code here.
	tree=BST(p[0])
	t=tree
	for i in range(1,len(p)):
		while(t!=None):
			prev=t
			if(p[i]>=t.value):
				t=t.right
			else:
				t=t.left
			
		if(p[i]>=prev.value):
			x=BST(p[i])
			prev.right=x
		else:
			x=BST(p[i])
			prev.left=x
		t=tree		
    return tree

