#Single element of stack
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

#Definig the Stack
class Stack(object):
    def __init__(self, top=None):
        '''
        initialises stack with optional Element parameter
        '''
        self.top = top

    def push(self, new_element):
        '''
        pushes an Element into the stack
        '''
        new_element.next = self.top
        self.top = new_element

    def pop(self):
        '''
        pops the top element from stack and returns it
        '''
        if self.top:
            deleted_element = self.top
            temp = deleted_element.next
            self.top = temp
            return deleted_element.value
        else:
            return 'stack is empty'
        
    def print_stack(self):
        '''
        prints the stack elements
        '''
        current = self.top
        while current:
            print(current.value)
            current = current.next
            
#Initialising stack elements
e1 = Element(0)
e2 = Element(1)
e3 = Element(2)

#Setting up the Stack
stack = Stack(e1)
stack.push(e2)
stack.push(e3)

#Printing the Stack
stack.print_stack()                     #prints "2 1 0"

#Popping elements from Stack
stack.pop()                             #outputs 2
stack.print_stack()                     #prints "1 0"

stack.pop()                             #outputs 1
stack.print_stack()                     ##prints "0"

stack.pop()                             #outputs 0
stack.print_stack()                     #prints nothing

stack.pop()                             #prints "stack is empty"
