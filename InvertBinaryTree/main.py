def invertBinaryTree(tree):
    # Write your code here.
	if(tree==None):
		return
	temp=tree.right
	tree.right=tree.left
	tree.left=temp
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
    pass


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


