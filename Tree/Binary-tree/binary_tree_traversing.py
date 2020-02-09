
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class binary_tree:
    def __init__(self,data):
        self.root = Node(data)

    def preorder_traverse(self,root,traversal):
        """root->left->right"""
        if root:
            traversal = traversal+str(root.data)+" - "
            traversal = self.preorder_traverse(root.left,traversal)
            traversal = self.preorder_traverse(root.right,traversal)
        return traversal

    def inorder_traverse(self,root,traversal):
        """left->root->right"""
        if root:
            traversal = self.inorder_traverse(root.left,traversal)
            traversal += (str(root.data)+" - ")
            traversal = self.inorder_traverse(root.right,traversal)
        return traversal

    def postorder_traverse(self,root,traversal):
        """left->right->root"""
        if root:
            traversal = self.inorder_traverse(root.left,traversal)
            traversal = self.inorder_traverse(root.right,traversal)
            traversal += (str(root.data)+" - ")
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type=="preorder":
            print(self.preorder_traverse(tree.root,''))
        elif traversal_type=="inorder":
            print(self.inorder_traverse(tree.root,''))
        elif traversal_type=="postorder":
            print(self.postorder_traverse(tree.root,''))
        else:
            print("this traversing is not supported")
            return False

# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7

# creating above tree
tree = binary_tree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.print_tree('preorder')
tree.print_tree('inorder')
tree.print_tree('postorder')
