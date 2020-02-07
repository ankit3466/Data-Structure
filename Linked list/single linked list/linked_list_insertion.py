
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Insertion:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self,data):
        ## this function will add node at the last
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self,data):
        ## this will add data at the beginning of the list
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,prev_node,data):
        new_node = Node(data)
        if not prev_node:
            print('Node is not in the list')
            return

        new_node.next = prev_node.next
        prev_node.next = new_node



s = Insertion()
s.print_list()
s.append('A')
s.append('B')
s.print_list()
print()
s.prepend('C')
s.print_list()
print()
s.insert_after_node(s.head.next,'E')
s.print_list()
