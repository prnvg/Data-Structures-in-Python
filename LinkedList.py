#A single element of the Linked List
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

#The linked list with head being the first element
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
        Appends an element to the list
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_element(self, position):
        """
        Returns element at specified position
        """
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """
        Inserts a new element at specific position
        """
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """
        Deletes first occurence of the specified value from the list
        """
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
             
            
    def print_list(self):
        current = self.head
        while current.next:
            print(current.value, "-> ", end = '')
            current = current.next
        print(current.value)
                
                

#Initialising some Elements
e1 = Element(0)
e2 = Element(1)
e3 = Element(2)
e4 = Element(3)
e5 = Element(4)

#Setting up the LinkedList
linked_list = LinkedList(e1)
linked_list.append(e2)
linked_list.append(e3)
linked_list.print_list()                     #outputs "0 -> 1 -> 2"


#Check element at specified position
print(linked_list.get_element(3).value)      #outputs 2

#Insert an element
linked_list.insert(e4,3)
linked_list.insert(e5,4)
linked_list.print_list()                     #outputs "0 -> 1 -> 3 -> 4 -> 2"



#Delete an element
linked_list.delete(2)
linked_list.print_list()                     #outputs "0 -> 1 -> 3 -> 4"
