

from httpx import head


class Node:
    def __init__(self, val):
        self.val =val 
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def reverse(self):
        myStack = []
        temp = self.head
        while temp is not None:
            myStack.append(temp.val)
            temp = temp.next
        temp = self.head
        while temp is not None:
            e = myStack.pop()
            temp.val = e
            temp = temp.next

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" <-> ")
            current = current.next
        print("None")

            
# Example usage:
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_head(30)
dll.insert_at_head(40)
dll.insert_at_head(50)
print("Original Doubly Linked List:")
dll.display()
dll.reverse()
dll.display()