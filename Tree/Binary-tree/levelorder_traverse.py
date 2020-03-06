class Queue(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class Binary_tree:
    def __init__(self,data):
        self.root = Node(data)

    def levelorder_traversing(self,start):
        if start is None:
            return
        q = Queue()
        q.enqueue(start)

        traversal = ""
        while not q.is_empty():
            
            node = q.dequeue()
            traversal += (str(node.data)+" - ")

            if node.left:
                q.enqueue(node.left)

            if node.right:
                q.enqueue(node.right)

        return traversal

# Calculate level order traversing of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5


tree = Binary_tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

a = tree.levelorder_traversing(tree.root)
print(a)
