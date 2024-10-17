# from collections import deque
# def precedance(operator):
#     if operator == '+' or operator == '-':
#         return 1
#     if operator == '*' or operator == '/':
#         return 2
#     return -1

# def infix_to_postfix(exp):
#     operators = ('+', '-', '*', '/' '(', ')')
#     res = []
#     stack = deque()
#     for char in exp: 
#         if char.isdigit():
#             res.append(char)
#         elif char == '(':
#             stack.append(char)
#         elif char == ')':
#             while stack and  stack[-1] != '(':
#                 res.append(stack.pop())
#                 stack.pop()
#         else:
#             while stack and precedance(stack[-1]) < precedance(char):
#                 res.append(stack.pop())
#     while stack:
#         res.append(stack.pop()) 
#     return res

# expression = "3+5(5-2)"
# print(infix_to_postfix(expression))






from collections import deque
def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    return -1

def infix_to_postfix(exp):
    res = []
    stack = deque()
    operators = ('+', '-', '*', '/', '(', ')')
    for char in exp:
        if char.isdigit():
            res.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                res.append(stack.pop())
            stack.append(char)

    while stack:
        res.append(stack.pop())
    return ''.join(res)

expression = "2*5-1+7"
print(infix_to_postfix(expression))