class TreeNodes:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        if self.root is None:
            self.root = TreeNodes(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNodes(key)
            else:
                self._insert(node.left, key) 
        else:
            if node.right is None:
                node.right = TreeNodes(key)
            else:
                self._insert(node.right, key)

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)
    
    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value

binarySearchTree = BinarySearchTree()

value = [9, 2, 1, 14, 5, 12, 11, 7, 3]
for val in value:
    binarySearchTree.insert(val)

max_value = binarySearchTree.find_max()
print("Маємо найбільше значення у дереві:", max_value)

