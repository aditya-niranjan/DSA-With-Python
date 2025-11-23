
from turtle import right
from unittest import result

from regex import R


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
        left = self.head
        right = self.head
        result = []
        while right.next is not None:
            right = right.next
        while left is not None and right is not None and left.val < right.val:
            total = left.val + right.val
            if total == target:
                result.append([left.val,right.val])
                left = left.next
                right = right.prev
            elif total > target:
                right = right.prev
            else:
                left = left.next
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
print(dll.find_pair_sum_to_target(5))
