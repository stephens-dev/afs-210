class Node:
 
    def __init__(self, data):
        self.data = data  
        self.next = None  
 
 
class LinkedList:
 
    def __init__(self):
        self.head = None
 
    
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
 
 

if __name__=='__main__':
 
    
    llist = LinkedList()
 
    llist.head = Node('PHP')
    second = Node('Python')
    third = Node('C#')
    fourth = Node('C++')
    fifth = Node('Java')
 
    llist.head.next = second; 
    second.next = third; 
    third.next = fourth
    fourth.next = fifth

 
    llist.printList()