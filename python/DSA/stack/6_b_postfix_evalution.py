from collections import deque

def postfix_evalution(postfix):
    stack = deque()
    # Add all postfix elemtns one by one
    for char in postfix:
        # If the postfix element is number then derectly push into stack
        if char.isdigit():
            stack.append(int(char))
        else:

            # If there is no number then pop into stack.
            num1 = stack.pop()  
            num2 = stack.pop()

            # If element of postfix is '+' then add both poped element
            if char == '+':
                stack.append(num1 + num2)

            # If element of postfix is '-' then substract both poped element
            elif char == '-':
                stack.append(num1 + num2)

            # If element of postfix is '*' then multiply both poped element
            elif char == '*':
                stack.append(num1 * num2)

            # If element of postfix is '/' then devide both poped element
            elif char == '/':
                stack.append(int(num1 / num2))
    # Pop the stack elements and print
    return stack.pop()
    
    
postfix = "23*"
result = postfix_evalution(postfix)
print(f"Your postfix is {postfix}, and postfix evalution is {result}")