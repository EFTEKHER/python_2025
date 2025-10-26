class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
        self.length=0
        self.head=None
        self.tail=None
    def push(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=None
        else:
            self.tail.next=new_node
            new_node.next=None
            self.tail=new_node
        self.length+=1 
    def isempty(self):
        if self.length==0:
            return True
        else:
            return False
        
    def __str__(self):
        temp=self.head
        result=""
        while temp:
            result+='\n'
            result+=str(temp.data)
            temp=temp.next
            
        return result[::-1]
    def pop(self):
        popped=None
        if self.isempty():
            return 'Empty'
        if self.length == 1:
            popped=self.tail.data
            self.head=None
            self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            popped=self.tail.data
            self.tail=temp
            self.tail.next=None
        self.length-=1
        return popped      
    def ispeek(self):
        if self.isempty():
            return 'Empty'
        else:
            return self.tail.data
            
            
if __name__=='__main__':
    st=stack()
    st.push(3)
    st.push(4)
    st.push(6)
    st.push(7)
    print(st)
    print('pop') 
    st.pop()
    print(st)
    print('peek')
    print(st.ispeek())