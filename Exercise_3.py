# Node class  
class Node:
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        NewNode = Node(new_data)
        
        if not self.head:
            self.head = NewNode
        
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        
        ptr.next = NewNode
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        if not self.head:
            print()

        slow = self.head
        fast = self.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.data)

# Driver code
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.printMiddle()
