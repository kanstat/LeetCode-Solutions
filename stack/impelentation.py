# implement a stack using linked list

# step1: create Node class

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

# step2: create stack class
class Stack:
    def __init__(self):
        self.head = None
        
    
    # check stack is empty
    def isempty(self):
        return self.head == None
    
    # add data to stack
    
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            
    # remove the element from stack (Head node or first node)
    
    def pop(self):
        if self.head==None:
            return "Stack is Empty"
        else:
            popednode = self.head
            self.head =     self.head.next
            popednode.next = None
            return popednode.data 
        
    # return the top most elemnt from the stack
    def peek(self):
        if self.head == None:
            return "Stack is empty"
        else:
            return self.head.data
        
    # display all the elements from the stack
    
    def display(self):
        temp = self.head
        if self.head == None:
            return "Stack is empty"
        else:
            while(temp!=None):
                print(temp.data, end = " ")
                temp = temp.next 
            return
        
        
        
        
# Driver code
if __name__ == "__main__":
  MyStack = Stack()
   
  MyStack.push(11)
  MyStack.push(22)
  MyStack.push(33)
  MyStack.push(44)
  MyStack.push(55)
  MyStack.push(66)
  MyStack.push(77)
  MyStack.push(88)
  MyStack.push(99)
  MyStack.push(110)
  


  # Display stack elements
  MyStack.display()
 
  # Print top element of stack
  print("\nTop element is ", MyStack.peek())
 
  # Delete top elements of stack
#   MyStack.pop()
#   MyStack.pop()

  # Display stack elements
  MyStack.display()
 
  # Print top element of stack
  print("\nTop element is ", MyStack.peek())
        
        
