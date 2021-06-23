import string
def inc(a,key):
	le=ord('z')-ord(a)
	nkey=(key-le)%26
	return(nkey)
def caesarCipherEncryptor(string, key):
    # Write your code here.
	l=list(string)
	for i in range(0,len(l)):
		if((ord(l[i])+key)>ord('z')):
			nkey=inc(l[i],key)
			l[i]=chr(ord('a')+nkey-1)
		else:
			l[i]=chr(ord(l[i])+key)
	s=""
	for i in l:
		s+=i
	return(s)
    pass

