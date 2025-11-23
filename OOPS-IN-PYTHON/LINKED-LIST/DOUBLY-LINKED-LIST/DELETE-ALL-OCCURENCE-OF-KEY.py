
from unittest import result


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
    def delete_occurence(self,target):
        temp = self.head
        prev = None
        new_head = self.head

        while temp is not None:
            if temp.val == target:
                if prev is not None:
                    prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = prev
                if temp == new_head:
                    new_head = new_head.next
            prev = temp
            temp = temp.next
        return new_head
    def display(self):
        current = self.head
        while current:
            print(current.val, end=" <-> ")
            current = current.next
        print("None")

            
# Example usage:
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(2)
dll.insert_at_head(3)
dll.insert_at_head(2)
dll.insert_at_head(5)
dll.display()
dll.delete_occurence(2)
dll.display()
