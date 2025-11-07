class Node:
  def __init__(self,val):
      self.val = val
      self.next = None


class SinglyLinkedList:
   def __init__(self):
      self.head = None

   def append(self,val):
      new_node = Node(val)
      if self.head == None:
         self.head = new_node
      else:
         curr = self.head
         while curr.next is not None:
            curr=curr.next
         curr.next = new_node
   def treversl(self):
        if self.head is None:
           print("sll is empty")
        else:
           curr = self.head
           while curr is not None:
              print(curr.val,end=" ")
              curr = curr.next


sll = SinglyLinkedList()
n = 5
for i in range(1,n+1):
   sll.append(i * i * 10)

sll.treversl()