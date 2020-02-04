"""
Use a stack data structure to convert integer values to their corresponding binary representation.

Example : 242

242 / 2 = 121 -> 0
121 / 2 = 60  -> 1
60 / 2  = 30  -> 0
30 / 2  = 15  -> 0
15 / 2  = 7   -> 1
7 / 2 = 3     -> 1
3 / 2 = 1     -> 1
1 / 2 = 0     -> 1

"""

from Stack_implement import Stack

def binary_convert(integer):
    s = Stack()
    if integer == 0:
        return 0

    while integer>0:
        y = integer%2
        s.push(y)
        integer = integer//2

    binary = ""
    while not s.is_empty():
        binary += str(s.pop())

    return binary

print(binary_convert(242))
print(binary_convert(0))
print(binary_convert(1))
print(binary_convert(1024))
print(binary_convert(8))


    
