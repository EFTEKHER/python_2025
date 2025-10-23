class Node:
    def __init__(self,value):
        self.prev=None
        self.next=None
        self.value=value
class dcll:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.prev=self.tail
            new_node.next=self.head
        else:
            new_node.prev=self.tail
            new_node.next=self.head
            self.tail.next=new_node
            # link head.prev to the new tail to keep circular prev pointer correct
            self.head.prev = new_node
            self.tail=new_node
        self.length+=1
    def __str__(self):
        temp=self.head
        result=""
        while temp:
            result+=str(temp.value)
            if temp.next is self.head:
                break 
            result+='<->'
            temp=temp.next
        return result
    def prepend(self,value):
        new_node=Node(value)
        if self.length ==0:
            self.head=new_node
            self.tail=new_node
            new_node.prev=self.tail
            new_node.next=self.head
            
        else:
            new_node.next=self.head
            new_node.prev=self.tail
            self.head.prev=new_node
            self.tail.next=new_node
            self.head=new_node
        self.length+=1
    def get_index(self,target):
        temp=self.head
        index=0
        while temp:
            if temp.value == target:
                return index
            if temp.next is self.head:
                break
            temp=temp.next
            index+=1
        return -1  
    def insert(self,index,value):
        new_node=Node(value)
        temp=self.head
        if index<0 or index>self.length:
            return 'out of bound'
        if index==0:
            self.prepend(value)
        else:
            for _ in range(index-1):
                temp=temp.next
            new_node.prev=temp
            new_node.next=temp.next
            temp.next.prev=new_node
            temp.next=new_node
            
        self.length+=1
    def  delete(self,index):
        if self.length==0:
            return "already Empty"
        elif self.length<index:
            return "out of bound"
        temp=self.head
        if index==0:
            self.head=self.head.next
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            for _ in range(index-1):
                temp=temp.next
            temp.next=temp.next.next
            temp.next.prev=temp
        self.length-=1
    def reverse(self):
        # Reverse a circular doubly linked list by swapping next and prev
        if self.length <= 1:
            return

        curr = self.head
        # swap next and prev for every node; after swapping, move to curr.prev
        for _ in range(self.length):
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev

        # after pointer swaps, swap head and tail references
        self.head, self.tail = self.tail, self.head

if __name__=='__main__':
    d=dcll()
    d.append(4)
    d.append(5)
    d.append(6)
    d.append(7)
    
    d.prepend(11)
    print(d) 
    d.insert(2,78)
    d.insert(0,99)
    d.insert(5,100)
    d.append(200)
    d.append(300)
    d.append(400)
    
    print(d)
    
    d.delete(3)
    print(d)
    d.reverse()
    print(d)