class Node:
    def __init__(self, data):
        self.left  = None
        self.data = data
        self.right = None
    
class BST:
    def create(self, data):
        return Node(data)
    def insert(self, node, data):
        if node is None:
            return self.create(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node
    def Inorder(self, node):
        if node is not None:
            self.Inorder(node.left)
            print(node.data, end= " ")
            self.Inorder(node.right)
    def Preorder(self, node):
        if node is not None:
            print(node.data, end= " ")
            self.Preorder(node.left)
            self.Preorder(node.right)
    def Postorder(self, node):
        if node is not None:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node.data, end=  " ")

tree = BST()

r = int(input("Enter the root! : "))

root = tree.create(r)

n = int(input("Enter the number of nodes! : "))
for i in range(n):
    tree.insert(root, int(input("Node : ")))
print(tree.Inorder(root))
print(tree.Preorder(root))
print(tree.Postorder(root))