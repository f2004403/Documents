class Queue(object):
	"""Basic implementation of singly linked queue."""
	def __init__(self):
		super(Queue, self).__init__()
		self.arr = []
		self.f = 0;
		self.r = -1;
	
	def __str__(self):
		"""docstring for __str__"""
		if self.isEmpty():
			return '[]'
		else:
			s = ""
			for i in range(self.f, self.r+1):
				s += str(self.arr[i])+"<-"
			s += "\n";
			return s
	
	def isEmpty(self):
		"""docstring for isEmpty"""
		if self.f > self.r:
			return True;
		return False
	
	def enqueue(self, item):
		"""docstring for enqueue"""
		self.r += 1;
		self.arr.insert(self.r,item);
	
	def dequeue(self):
		"""docstring for dequeue"""
		if self.isEmpty():
			raise Exception("Empty queue");
		self.f += 1;
	
	def size(self):
		"""docstring for size"""
		return self.r - self.f + 1

def main():
	"""Just to test"""
	q = Queue();
	print "Initial size = ",q.size();
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.enqueue(1)
	print q;
	q.dequeue();
	print q
	q.dequeue();
	print q
	q.dequeue();
	print q
	q.dequeue();
	print q
	q.dequeue();
	print q
	q.dequeue();
	print q

if __name__ == '__main__':
	main()