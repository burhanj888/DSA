class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None
    
   def set_data(self,data):
      self.data = data
    
   def get_data(self):
      return self.data
   
   def set_next(self, next):
      self.next = next

   def get_next(self):
      return self.next
   
   def has_next(self):
      return self.next != None

class LinkedList(object):
   def __init__(self, node = None):
    #   self.length = 0
      self.head = node

   def listprint(self):
      printval = self.head
      while printval is not None:
         print(printval.data)
         printval = printval.next


node1 = Node("Mon")

lList = LinkedList()
lList.head = node1

node2 = Node("Tue")
node3 = Node("Wed")

lList.head.next = node2
node2.next = node3

lList.listprint()

