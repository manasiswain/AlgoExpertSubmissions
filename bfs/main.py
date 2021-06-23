# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        l=[]
		l.append(self)
		array.append(self.name)
		while(l!=[]):
			l.pop(0)
			l.extend(self.children)
			if(l==[]):
				break
			self=l[0]
			array.append(self.name)
		print(array)
		return(array)
        pass

