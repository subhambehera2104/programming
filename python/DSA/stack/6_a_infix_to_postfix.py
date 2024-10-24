from collections import deque
def precedence(operator):
    # In this function will check the operator precedence

    if operator == '+' or operator == '-': # If the operator is + or - then the precedence is 1
        return 1
    if operator == '*' or operator == '/': # If the operator is * or / then the precedence is 2
        return 2
    # else return 0 or -1
    return -1

def infix_to_postfix(exp):
    res = [] # Create a result stack for printing result elements
    stack = deque() # Create a stack for storing operators
    operators = ('+', '-', '*', '/', '(', ')') 
    for char in exp: 
        
        # If expression is number, then directly store in res stack
        if char.isdigit():
            res.append(char)

        # If the operator will be open breacket '(' then push into main stack
        elif char == '(':
            stack.append(char)

        # If the operator will be colse breaket ')' then pop until finding open breacket '(' and also print the all poped elements
        elif char == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()

        # If the entered operator's precedence is less than or equal to precedence of top element of stack, then you should pop and print thel poped elements
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                res.append(stack.pop())
            stack.append(char)
    # If stack is not empty, then you can pritn the reamining operators
    while stack:
        res.append(stack.pop())
    return ''.join(res)

expression = "2*5-1+7"
print(infix_to_postfix(expression))