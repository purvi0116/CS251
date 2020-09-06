
#IS THE LIST RETURNED BY ALLTREES CORRECT?? OR DO YOU HAVE TO RETURN SOMETHING ELSE
class Node(object):
	"""
	Node contains two objects - a left and a right child, both may be a Node or both None,
	latter representing a leaf
	"""
	def __init__(self, left=None, right=None):
		super(Node, self).__init__()
		self.left = left
		self.right = right

	def __str__(self):
		"""
		Default inorder print
		"""
		if self.left is None and self.right is None:
			return "(   )"
		else:
			return "( " + str(self.left) + " " + str(self.right) + " )"

	def __eq__(self, other):
		if self.left is None and self.right is None:
			return other.left is None and other.right is None
		elif other.left is None and other.right is None:
			return False
		else:
			return self.left == other.left and self.right == other.right


def mirrorTree(node):
	"""
	Returns the mirror image of the tree rooted at node
	"""
	if node.left is None and node.right is None:
		return node
	else:
		node=Node(mirrorTree(node.right),mirrorTree(node.left))
		return 	node
	


LL={}  #dict for memoization 
def allTrees(n):
	"""
	Returns a list of all unique trees with n internal nodes
	"""
	if(n in LL): 
		return LL[n]
	nodeList=[]
	if n==0:
		nodeList=[Node()]
		LL[n]=nodeList
		return nodeList
	else:
		for i in range(0,n):
			nodeList+=[Node(l,r) for l in allTrees(i) for r in allTrees(n-1-i)]	
		LL[n]=nodeList
		return nodeList	

def allSymTrees(n):
	"""
	Returns a list of all unique symmetrical trees with n internal nodes
	"""
	if(n==0): 
		return [Node()] 
	if(n%2==0):
		return []
	else:
		nodeSymList=[Node(l,mirrorTree(l)) for l in allTrees((n-1)//2) ]		
		return nodeSymList

if __name__ == '__main__':
	for x in allSymTrees(int(input())):
		print(x)
	node = Node(Node(Node(), Node()), Node())
	print(node)

