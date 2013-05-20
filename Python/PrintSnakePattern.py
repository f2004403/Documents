def main():
	"""docstring for main"""
	a = [
		[1,2,3],
		[4,5,6],
		[7,8,9]]
	for i in range(len(a)):
		for j in range(len(a[i])):
			print a[i][j],"->",
	
	print "\nActual method - Note that only one index changes at a time"
	visited = set([])
	toVisit = []
	for i in range(len(a)):
		for j in range(len(a[i])):
			toVisit.append((i,j));
	
	start = (0,0)
	while (len(toVisit) > 0):
		if toVisit.contains(start):
			print start;
			toVisit.remove(start):
			start = lis
		
		
		

	pass
if __name__ == '__main__':
	main()