class Stack(object):
	
	def __init__(self):
		self.arr = [];
		self.top = -1;
	
	def top(self):
		"""Return top element"""
		if self.isEmpty():
			raise Exception("Stack empty")
		else:
			return self.arr[self.top]
	
	def isEmpty(self):
		"""Empty or not"""
		if self.top == -1:
			return True;
		else:
			return False
	
	def size(self):
		"""Give size of the stack"""
		if self.isEmpty():
			return 0;
		else:
			return self.top+1;
	
	def push(self, item):
		"""Add item to top of stack"""
		self.top+=1;
		self.arr.insert(self.top, item);
	
	def pop(self):
		"""Pop item"""
		if self.isEmpty():
			raise Exception("Cant pop from empty stack")
		item = self.arr[self.top];
		self.arr.pop(self.top)
		self.top-=1;
		return item;
	
	def __str__(self):
		"""docstring for __str__"""
		s=""
		for i in range(self.top+1):
			s+=str(self.arr[i])+" -> "
		s+="\n"
		return s

def main():
	"""Testing.."""
	s = Stack();
	print s
	print "s.isEmpty()=",s.isEmpty();
	s.push(1)
	s.push(2)
	s.push(3)
	print s;
	print s.size()
	x = s.pop();
	x = s.pop();
	x = s.pop();
	print s;
	print s.size()
	
	pass
if __name__ == '__main__':
	main()