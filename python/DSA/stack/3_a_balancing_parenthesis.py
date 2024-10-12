#Balancing parenthesis using stack
def isexp(expression):
    stack = []
    for char in expression:
        #Opening brakets
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            #if stack is empty
            if not stack:
                return False
            
            #Check the expression
            top = stack.pop()
            if(top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and char != ']'):
                return False
    return len(stack) == 0 #check if stack is empty

expression = input("Enter math expression ")
if isexp(expression):
    print("Your syntax is correct")
else:
    print("Invalid syntax")