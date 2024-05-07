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
            print(f"{temp.data}--->",end="")
            temp = temp.next
            
    def pushbegning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def pushinend(self,new_data):
        new_node = Node(new_data)
        
        # case 1 : when linked list is empty
        if self.head is None:
            self.head = new_node
            return
        
        # case2 : when linken list is not empty then we have to traverse till the end
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        
    
        
        
        
        
                    
            
    
        

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
    
    # ll.pushbegning(6)
    ll.pushinend(6)
    
    print()
    
    ll.traverse_list()
    
    