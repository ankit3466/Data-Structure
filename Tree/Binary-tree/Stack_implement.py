"""
Stack Data Structure.
"""

class Stack:

    def __init__(self):
        # this function will initilize the stack.
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):

        # this function will return top element of stack
        if not self.is_empty():
            return self.items[-1]

    def display_stack(self):
        return self.items

    
