class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursively(self.root, new_node)

    def _insert_recursively(self, current_node, new_node):
        if new_node.data < current_node.data:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursively(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursively(current_node.right, new_node)

    def display_inorder(self):
        self._display_inorder_recursively(self.root)
        print()

    def _display_inorder_recursively(self, current_node):
        if current_node:
            self._display_inorder_recursively(current_node.left)
            print(current_node.data, end=' ')
            self._display_inorder_recursively(current_node.right)

# Example usage
bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

bt.display_inorder()
