# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(tree):
    # Write your code here.
	l=[]
	array=[]
	b=[]
	ct=0
	while(1):
		while(tree!=None):
			l.append(tree)
			tree=tree.left
		if(len(l)==0):
			break
		tree=l[-1]
		array.append([ct,tree.value])
		b.append(tree.value)
		ct+=1
		l.pop(-1)
		tree=tree.right
		if(tree!=None):
			ct-=1
	return([array,b])
		
def validateBst(tree):
    # Write your code here.
	g=inOrderTraverse(tree)
	l=g[0]
	b=g[1]
	if(b==sorted(b)):
		for i in range(0,len(l)):
			if(b.count(l[i][1])>1):
				for j in range(0,len(l)):
					if(i!=j and l[j][1]==l[i][1]):
						if(l[j][0]!=l[i][0]):
							return(False)
		return(True)
	else:
		return(False)
						
			
	print(l)
		
    pass

