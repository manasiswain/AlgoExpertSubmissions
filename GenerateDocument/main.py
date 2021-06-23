def generateDocument(characters, document):
    # Write your code here.
	c={}
	d={}
	ch=list(characters)
	if(document==""):
		return True
	for i in set(characters):
		c[i]=0
	for i in set(document):
		if(i not in ch):
			return False
		else:
			d[i]=0
	for i in characters:
		c[i]+=1
	for i in document:
		d[i]+=1
	for i in document:
		if(d[i]>c[i]):
			return False
	return True

