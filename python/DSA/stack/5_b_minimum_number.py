from collections import deque
class MinStack:
    def __init__(self):
        self.main_stack = deque()
        self.min_stack = deque()
    def push(self, element):
        self.main_stack.append(element)

        if len(self.min_stack) == 0:
            self.min_stack.append(element)
        elif(element <= self.min_stack[-1]):
                self.min_stack.append(element)
        return element
    
    def pop(self):
        if self.min_stack:
            poped_element = self.main_stack.pop()
            if poped_element == self.min_stack[-1]:
                self.min_stack.pop()
            return poped_element
        else:
            print("Your stack is empty")
        
    def minimum(self):
        return self.min_stack[-1]

s = MinStack()
print("Inserted ", s.push(10))
print("Minimum is ", s.minimum())
print("Again inserteed ", s.push(2))
print("Now minimum is ", s.minimum())
print("Inserted ", s.push(20), "and ", s.push(5))
print("Minimum is ", s.minimum())
print("Removed element is ", s.pop())
print("Minimum is ", s.minimum())