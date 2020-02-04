
from Stack_implement import Stack

def reverse_string(string):

    x = len(string)
    s = Stack()
    for i in string:
        s.push(i)
    out = ''.join([s.pop() for i in range(x)])

    return out


print(reverse_string('Hello'))
print(reverse_string('this'))
print(reverse_string('is'))
print(reverse_string('Data Structure'))

# without Stack------
# -------------------print(string[::-1])

