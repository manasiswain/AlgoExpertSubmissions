 Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		isp=0
		x=value
		p=BST(value=x)
		while(self!=None):
			if(value>=self.value):
				isp=1
				prev=self
				self=self.right
			else:
				isp=2
				prev=self
				self=self.left
		if(isp==1):
			prev.right=p
		elif(isp==2):
			prev.left=p
		print("done")
        return self

    def contains(self, value):
        # Write your code here.
		while(self!=None):
			if(self.value==value):
				return(True)
			elif(value>=self.value):
				self=self.right
			else:
				self=self.left
		return(False)

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		isp=0
		if(self.right==None and self.left==None):
			return(self)
		while(self!=None):
			if(value==self.value):
				p=self
				if(self.right==None and self.left==None):
					if(isp==1):
						prev.right=None
						
					elif(isp==2):
						prev.left=None
					x=self
				    self=p
				    del(x)
					break
				prev=self
				self=self.right
				if(self==None):
					x=prev.left
					prev.value=x.value
					prev.left=x.left
					del(x)
					self=p
				else:
					ct=0
				
					while(self.left!=None):
						ct+=1
						prev=self
						self=self.left
					p.value=self.value
					if(ct==0):
						prev.right=self.right
					else:
						prev.left=None
					x=self
					self=p
					del(x)
					break
		    elif(value>=self.value):
				isp=1
			    prev=self
				aa=self
				self=self.right
			else:
				isp=2
				prev=self
				aa=self
				self=self.left
		
        return self

