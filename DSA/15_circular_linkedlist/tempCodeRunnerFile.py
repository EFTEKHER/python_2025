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
if __name__=='__main__':
    cs=CircularLinkedList()
    cs.append(4)
    cs.append(5)
    cs.append(6)
    cs.append(7)
    print(cs)
    
                     
            
                    