#Balancing parenthesis using deque library

from collections import deque
def isexp(expression):
    stack = deque()

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            return False
            if not stack:
                return False
                
        top = stack.pop()
        if(top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and  char != ']'):
            return False

    return len(stack) == 0

expression = input("Enter expression ")
if isexp(expression):
    print("Your syntax is correct")
else:
    print("Invalid syntax")