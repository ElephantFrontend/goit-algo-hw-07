class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key) 
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)
    
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

BinarySearchTree = BinarySearchTree()

value = [9, 2, 1, 14, 5, 12, 11, 7, 3]
for val in value:
    BinarySearchTree.insert(val)

min_value = BinarySearchTree.find_min()
print("Маэмо найменьше значення у дереві:", min_value)
