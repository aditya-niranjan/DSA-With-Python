class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def Insert(self, val):
        new_node = Node(val)
        # If list is empty
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            # Move to the end of the list
            while current.next is not None:
                current = current.next
            # Add new node at the end
            current.next = new_node

    def Travle(self):
        if self.head is None:
            print("Linked list is empty!!")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" -> ")
                current = current.next
            print("None")


# ----------------------------
# Test the Linked List
# ----------------------------

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sll = LinkedList()
for num in nums:
    sll.Insert(num)

print("Linked List elements:")
sll.Travle()
