from collections import deque
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def isLeaf(node):
    return node.left is None and node.right is None
 
def printRootToLeafPaths(node, path,paths):
    if node is None:
        return
    path.append(node.value)

    if isLeaf(node):
		paths.append(list(path))

    printRootToLeafPaths(node.left, path,paths)
    printRootToLeafPaths(node.right, path,paths)

    path.pop()

def printRootToLeafPath(node,paths):

    path = deque()
    printRootToLeafPaths(node,path,paths)
def binaryTreeDiameter(tree):
    # Write your code here.
	paths=[]
	t=tree
	printRootToLeafPath(tree,paths)
	paths.sort(key=len)
	print(paths)
	if(len(paths)==1):
		return(len(paths[0])-1)
	z=paths[-1]
	v=paths[-2]
	q=len(paths[-1])
	isp=0
	for i in paths:
		if(len(i)<q):
			isp=1
			break
		else:
			isp=0
				
	if(isp==0):
		
		v=paths[0]
		ct=0
		for i in range(0,len(z)):
			if(z[i] in v):
				v.pop(i)
				ct+=1
			else:
				break
		i=0
		while(ct>0):
			z.pop(i)
			ct-=1
			i+=1
		a=len(paths[-1])
	    b=len(paths[0])
        return(a+b)
		
	ct=0
	for i in range(0,len(z)):
		if(z[i] in v):
			v.pop(i)
			ct+=1
		else:
			break
	i=0
	while(ct>0):
		z.pop(i)
		ct-=1
		i+=1
	a=len(paths[-1])
	b=len(paths[-2])
    return(a+b)

