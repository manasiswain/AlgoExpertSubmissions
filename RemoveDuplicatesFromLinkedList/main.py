# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	l=[]
	k=linkedList
	prev=linkedList
	if(linkedList!=None):
		while(linkedList!=None):
			if(linkedList.value not in l):
				l.append(linkedList.value)
				prev=linkedList
			    linkedList=linkedList.next
			else:
				
				prev.next=linkedList.next
				temp=linkedList
				linkedList=linkedList.next
				del temp
		
			
		return k	
	else:
		return None

