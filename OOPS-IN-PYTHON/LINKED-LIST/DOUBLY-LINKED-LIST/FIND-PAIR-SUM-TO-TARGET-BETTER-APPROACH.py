
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
    def find_pair_sum_to_target(self,target):
        temp = self.head
        my_set = set()
        result = []

        while temp is not None:
            remaining = target - temp.val
            if remaining in my_set:
                result.append([remaining,temp.val])
            my_set.add(temp.val)
            temp = temp.next
        return result
    def display(self):
        current = self.head
        while current:
            print(current.val, end=" <-> ")
            current = current.next
        print("None")

            
# Example usage:
dll = DoublyLinkedList()
dll.insert_at_head(9)
dll.insert_at_head(8)
dll.insert_at_head(6)
dll.insert_at_head(5)
dll.insert_at_head(4)
dll.insert_at_head(2)
dll.insert_at_head(1)
dll.display()
# dll.find_pair_sum_to_target(7)
print(dll.find_pair_sum_to_target(7))
