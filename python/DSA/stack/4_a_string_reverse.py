from collections import deque
stack = deque()

def push(element):
    for char in element:
        stack.append(char)
def pop(element):
    for i in range(0,len(stack)):
        if len(stack)>0:
            print(f"{stack.pop()}", end="")

element = input("Enter charters ")
push(element)
pop(element)