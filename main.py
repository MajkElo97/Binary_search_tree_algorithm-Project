class Tree:

    def __init__(self, value, content=None):
        self.left = None
        self.right = None
        self.value = value
        self.content = content

    def insert(self, value, content=None):
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        elif value > self.value:
            if self.right is None:
                self.right = Tree(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    def find(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)

        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)


tree = Tree(5)
tree.insert(4)
tree.insert(11, "Test content")
tree.insert(2)
tree.insert(6)

tree.find(7)

tree.inorder_traversal()
tree.preorder_traversal()
tree.postorder_traversal()

print(tree.find(11).content)
