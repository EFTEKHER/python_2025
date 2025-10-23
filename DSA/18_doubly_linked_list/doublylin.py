class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
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
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    def __str__(self):
        temp=self.head
        result=""
        while temp:
            result+=str(temp.data)
            
            if temp.next is None:
                break
            temp=temp.next
            result+=' <-> '
        return result
    def prepend(self,value):
        new_node=Node(value)
        
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1   
    def insert(self,index,value):
        new_node=Node(value)
        if index<0 or index>self.length:
            print("out of bound")
            return None 
        if self.length==0:
            self.prepend(value)
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next 
            new_node.next=temp.next
            new_node.prev=temp
            temp.next.prev=new_node
            temp.next=new_node
        self.length+=1
    def get_index(self, target):
        temp=self.head
        index=0
        while temp:
            if temp.data==target:
                return index
            temp=temp.next
            index+=1
        return -1
    def set_index(self,index,value):
        # bounds checks
        if self.head is None or self.length == 0:
            print("List is empty")
            return False
        if index < 0 or index >= self.length:
            print("Index out of bounds")
            return False

        temp = self.head
        for i in range(index):
            temp = temp.next

        # Node stores value in `data` attribute
        temp.data = value
        return True
            
                
    def reverse(self):
        temp=self.tail
        while temp:
            
            temp.prev,temp.next=temp.next,temp.prev
            temp=temp.next
        self.head,self.tail=self.tail,self.head
    def search(self, target):
        temp=self.head
        while temp:
            if temp.data==target:
                return  self.get_index(target)
            temp=temp.next
        return False
    def delete(self,index):
        if self.length ==0:
            return None
        elif index<0 or index>self.length:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
        elif index==0:
            self.head=self.head.next
            self.head.prev=None
            self.length-=1
        elif index==self.length-1:
            self.tail=self.tail.prev
            self.tail.next=None
            self.length-=1      
            
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next 
            temp.next=temp.next.next
            temp.next.prev=temp
            self.length-=1    
                
    
        
if __name__=="__main__":
    d= DLL()
    d.append(4)
    d.append(5)
    d.append(6)
    d.prepend(9)
    d.insert(2,11)
    print(d)
    d.reverse()
    print(d.search(6))
    
    
    print(d)
    d.delete(4)
    print(d)
    d.set_index(2,23)
    print(d)
            
                          