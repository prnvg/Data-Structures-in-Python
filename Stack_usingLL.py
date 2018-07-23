class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, new_element):
        new_element.next = self.top
        self.top = new_element

    def pop(self):
        if self.top:
            deleted_element = self.top
            temp = deleted_element.next
            self.top = temp
            return deleted_element.value
        else:
            return 'stack is empty'
        
    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next
