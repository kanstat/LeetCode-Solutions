class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        
        
        
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
        
    def traverse_list(self):
        if self.head == None:
            print("Linked List is empty")
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
            
    def pushbegning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    
        
    
        
        
        
        
                    
            
    
        

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    
    ll = LinkedList()
    ll.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    
    
    ll.traverse_list()