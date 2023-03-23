
class Node:
    def __init__(self,value):
        self.value = value 
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if (self.root == None):
            self.root = new_node
        else:
            currentNode = self.root
            while(True):
                if (value < currentNode.value):
                    if (not currentNode.left):
                        currentNode.left = new_node
                        return
                    currentNode = currentNode.left
                else:
                    if( not currentNode.right):
                        currentNode.right = new_node
                        return
                    currentNode = currentNode.right

    def lookup(self,value):
        if (not self.root):
            return False
        currentnode = self.root 
        while (currentnode):
            if (value < currentnode.value):
                currentnode = currentnode.left
            elif( value > currentnode.value):
                currentnode = currentnode.right
            elif ( value == currentnode.value):
                return True
        return False

BST = BinarySearchTree()
BST.insert(34)
BST.insert(56)
BST.insert(67)
BST.insert(5)
BST.insert(8)
print(BST.lookup(980))
