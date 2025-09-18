class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None 
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1  
        print(f"Appended {value} to the list.")    
        print(f"Current list length: {self.length}")
        
if __name__=="__main__":
    ll=LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    # Print the linked list
    current=ll.head
    while current:
        print(current.value, end=" -> ")
        current=current.next
    print("None")        