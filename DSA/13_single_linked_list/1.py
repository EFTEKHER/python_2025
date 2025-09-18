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
    def __str__(self):
        temp=self.head
        result=""
        while temp is not None:
            result += str(temp.value) + " -> "
            temp=temp.next
        
        return result
    def insertathead(self,value):
        temp=self.head
        
        new_node=Node(value)
        
        new_node.next=temp
        
        self.head=new_node
        
        self.length+=1
        
    def insertatindex(self,index,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        elif index==0:
            self.insertathead(value)
        elif index<-1 or index>self.length:
            return None
        else:
            temp=self.head
            for _ in range(index-1):
                prevnode=temp.next
                temp=prevnode
                nextnode=temp.next     
                temp.next=new_node
                new_node.next=nextnode
        self.length+=1

if __name__=="__main__":
    ll=LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.insertathead(16)
    ll.insertatindex(3,25)
    ll.insertatindex(0,5)
    # Print the linked list
    print(ll)