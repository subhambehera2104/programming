from collections import deque

class MaxStack:
    def __init__(self):
        """
        In ths scope, first of all you should taake tow stack. stack 1 should store all elements and 
        stack 2 should storemaximum numbers in ascending order.
        """
        self.main_stack = deque()
        self.max_stack = deque() # Maximum stack for storing maximum numbers in ascending order 

        """
        Function of push method:

        Bascily all elements can push into main stack but can't push to maximum stack. While you push the first element, you can push
        both main stack and max stack. while the next element push to main stack then you should check if the top element of max 
        stack is greater than pushed element or equal to pushed element, then push into maximum stack. otherwise can push into main stack.
        """
    def push(self, element):
        self.main_stack.append(element)
        if len(self.max_stack) == 0: 
            # If main stack or max stack is empty, then push the element into both of the stack
           self.max_stack.append(element)
        elif element >= self.max_stack[-1]:
            # If element is greater than to top element of max_stack or equal to max_stack's top element, then push
            self.max_stack.append(element)
        return element # I want to display the print element so that I'm writed return element

        """
        Function of pop method:
        While you pop an element from main stack, then you should check if poped element is equal to top element of maximum 
        stack then you can pop the element from maximum stack. otherwise you can pop only from main stack.
        """
    def pop(self):
        if self.max_stack:
            poped_element = self.main_stack.pop()

            if poped_element == self.max_stack[-1]:
                self.max_stack.pop()
            return poped_element
        else:
            # Directly print you stack is empty
            print("Your stack is empty")
            
    # You should create a function for printing maximum element
    def maximum(self):
        return self.max_stack[-1]
         

s = MaxStack()
print("Inserted ", s.push(10))
print("Maximum is ", s.maximum())
print("Again inserteed ", s.push(2))
print("Now maximum is ", s.maximum())
print("Inserted ", s.push(20), "and ", s.push(5))
print("Maximum is ", s.maximum())
print("Removed element is ", s.pop())
