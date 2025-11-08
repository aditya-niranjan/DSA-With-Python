class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

    def reverseList(self,head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.print_list()
ll.reverseList()