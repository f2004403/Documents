class Node(object):
	"""docstring for Node"""
	def __init__(self, data=None, next=None):
		super(Node, self).__init__()
		self.data = data;
		self.next = next;


class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		super(LinkedList, self).__init__()
		self.head = None
		
	
	def findPositionToInsert(self, item):
		"""returns pointer to node before the item """
		prev = None;
		cur = self.head;
		while(cur != None):
			
			print prev.data if prev != None else None, cur.data;
			if cur.data >= item:
				return prev;
			(prev, cur) = (cur, cur.next)
	
	
	def insertSorted(self, item):
		"""docstring for insertSorted"""

		if self.size() == 0:
			self.head = Node(item, None);
		prev = self.findPositionToInsert(item)
		if prev == None:
			self.head = Node(item, self.head)
		else:
			newNode = Node(item,prev.next);
			prev.next = newNode;

	
	def insertAtHead(self, item):
		"""docstring for insert"""
		if self.head == None:
			self.head = Node(item, None);
		else:
			oldHead = self.head;
			self.head = Node(item, oldHead);
		pass
		
	
	def size(self):
		"""docstring for insert"""
		cur = self.head;
		size = 0;
		while(cur != None):
			size += 1;
			cur = cur.next;
		return size;	

	
	def delete(self, item):
		"""docstring for delete"""
		# empty list
		if self.size() == 0:
			raise Exception("Item not found in empty list");
		
		itemFoundFlag = False;
		# item to be deleted at the head
		cur = self.head;
		if (cur.data == item):
			self.head = cur.next;
			itemFoundFlag = True;
			return;
		else:
			while (cur != None):
				prev = cur;
				cur = cur.next;
				if cur.data == item:
					itemFoundFlag = True
					prev.next = cur.next; 
					break; # Only delete first item
			
		
		# item to be deleted at the end
		
		if itemFoundFlag == False:
			raise Exception("Item not found in list");
		# item not found in the list
		pass
	
	def __str__(self):
		"""docstring for __str__"""
		cur = self.head;
		s=""
		while(cur != None):
			s+= str(cur.data)+"->"
			cur = cur.next;
		return s;

def main():
	"""docstring for main"""
	linkedList = LinkedList();
	# linkedList.insertAtHead(3);
	# linkedList.insertAtHead(4);
	# linkedList.insertAtHead(1);
	# print linkedList
	# print linkedList.size()
	# linkedList.delete(2)
	# print linkedList
	# linkedList.delete(3)
	# print linkedList
	# linkedList.delete(1)
	# print linkedList
	
	
	linkedList.insertSorted(1);
	linkedList.insertSorted(2);
	linkedList.insertSorted(3);
	print linkedList
	
	pass
	
if __name__ == '__main__':
	main()
