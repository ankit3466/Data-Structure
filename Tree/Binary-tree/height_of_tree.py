
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self,data):
        self.root = Node(data)

    def height(self,node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1+max(left_height,right_height)


# Calculate height of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5
# 
tree = Binary_tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.height(tree.root))

tree2 = Binary_tree(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)
tree2.root.left.left = Node(4)
tree2.root.left.right = Node(5)
tree2.root.right.left = Node(6)
tree2.root.right.left.right = Node(7)
tree2.root.right.left.right.right = Node(8)

print(tree2.height(tree2.root))

