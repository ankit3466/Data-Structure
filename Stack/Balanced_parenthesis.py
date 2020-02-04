
"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.

"""

# importing stack module that we build previously

from Stack_implement import Stack


def is_match(p1,p2):
    if p1=='[' and p2==']':
        return True
    elif p1=='{' and p2=='}':
        return True
    elif p1=='(' and p2==')':
        return True
    else:
        return False
    

def check_paren(input_string):

    x = len(input_string)
    s = Stack()
    index = 0
    is_balanced = True

    while index < x and is_balanced:
        paren = input_string[index]

        if paren in '{[(':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print(check_paren('{}'))
print(check_paren('{{}{}{}{}{}}'))
print(check_paren('{[][[[[]}'))
print(check_paren('{([{}]())}'))
print(check_paren('{[[[[))))()}'))

                
