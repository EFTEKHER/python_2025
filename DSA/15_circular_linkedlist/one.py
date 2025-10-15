class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1
    def __str__(self):
        temp=self.head
        result=""
        while temp:
            result+=str(temp.data)
            if temp.next == self.head:
                break
            result+='->'
            temp = temp.next 
        return result
    def prepend(self,value):
        
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
        self.length+=1
    def insert(self,index,value):
        new_node=Node(value)
        if index<0 or index>self.length:
            print("out of bound")
            return 
        if self.length==0:
            self.prepend(new_node.value)
        elif self.length==index-1:
            self.tail.next=new_node
            
            new_node.next=self.head  
            self.tail=new_node  
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
        self.length+=1
    def pop_first(self):
        x=None
        if self.length==0:
            return None
        else:
            popped=self.head.data
            x=popped
            self.head=self.head.next
            self.tail.next=self.head
            
            self.length-=1
        return x
    def pop(self):
        val=None
        if self.length == 0:
            return None
        else:
            temp=self.head
            while temp.next != self.tail:
                temp=temp.next
            val=self.tail.data 
            self.tail=temp
            self.tail.next=self.head
            self.length-=1   
        return val
    def remove(self,index):
        val=None
        if self.length==0:
            return None
        elif index<0 or index>self.length:
            return "out of bound"
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
                
            val=temp.data
            temp.next=temp.next.next
            self.length-=1 
        return val
    def get_value(self,index):
        if index<0 or index>self.length:
            return "out of bound"
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp.data     
                    
                
                
                
                
                        
                       
if __name__=='__main__':
    cs=CircularLinkedList()
    cs.append(4)
    cs.append(5)
    cs.append(6)
    cs.append(7)
    cs.prepend(1)
    cs.insert(1,44)
    cs.insert(6,32)
    print(cs)
    
    print(cs.pop_first())
    
    print(cs)
    print(cs.pop())

    print(cs)
    print(cs.remove(8))
    print(cs)
    print(cs.get_value(3))
    
                     
            
                    