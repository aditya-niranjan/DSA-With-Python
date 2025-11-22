
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def length_of_loop(self):
        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:   # cycle found
                # Step 2: Find loop length
                fast = fast.next
                count = 1
                while fast != slow:
                    fast = fast.next
                    count += 1
                return count

        return None 
                
                    

# Create all nodes first
n5  = Node(5)
n9a = Node(9)   # first 9
n1a = Node(1)   # first 1
n7  = Node(7)
n6  = Node(6)
n1b = Node(1)   # second 1 inside the big loop
n9b = Node(9)   # second 9 inside the big loop
n2  = Node(2)
n8  = Node(8)

# Connect the main chain
n5.next = n9a
n9a.next = n1a

# Split from n1a
n1a.next = n7      # upper path → 7 → 6 → 1 → 9 → 2 → 8 → back to 1a
n8.next = n1a      # lower path → 8 → back to 1a

# Build the big cycle
n7.next = n6
n6.next = n1b
n1b.next = n9b
n9b.next = n2
n2.next = n8    # 2 → 8 → back to n1a (closing the lower loop)

# HEAD of the entire linked list
head = n5

print(n5.length_of_loop())

