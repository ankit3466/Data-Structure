
class Queue:
    def __init__(self):
        self.items = []

    def length(self):
        return len(self.items)

    def enqueue(self,data):
        self.items.insert(0,data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def print_queue(self):
        print(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


##### Example ########

q = Queue()

print(q.length())
print(q.is_empty())
q.print_queue()
q.enqueue(23)
q.enqueue(25)
q.print_queue()
print(q.dequeue())
q.print_queue()
