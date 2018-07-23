#Single element of queue
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
#Defining the Queue
class Queue(object):
    def __init__(self, front=None):
        '''
        initialises queue with optional parameter
        '''
        self.front = Element(front)

    def enqueue(self, new_element):
        '''
        adds an element to the queue
        '''
        if self.front:
            current = self.front
            while current.next:
                current = current.next
            current.next = Element(new_element)
        else:
            self.front = Element(new_element)

    def dequeue(self):
        '''
        removes the first element from queue and returns it
        '''
        if self.front:
            deleted_element = self.front.value
            self.front = self.front.next
            return deleted_element
        else:
            return 'queue is empty'
        
    def print_queue(self):
        '''
        prints the queue elements
        '''
        current = self.front
        if current:
            while current.next:
                print(current.value, ', ', end='')
                current = current.next
            print(current.value)
            
        else:
            print('queue is empty')
