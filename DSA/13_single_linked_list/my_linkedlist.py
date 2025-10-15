class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        current = self.head
        res = str(current.value)
        while current.next:
            res += "->"
            res += str(current.next.value)
            current = current.next
        return res

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1

    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
        return True

    def pop_first(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return popped_node.value

    def pop(self):
        if self.head is None:
            return None
        current = self.head
        prev = self.head
        while current.next:
            prev = current
            current = current.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current.value
    def remove(self,index):
        if self.head is None or self.length==0 or index<0 or index>=self.length:
            return None
        prev=self.head
        
        
        for _ in range(index-1):
            prev=prev.next
        prev.next=prev.next.next
        self.length-=1    
        
            
            

            
                                     
                
if __name__=="__main__":
    my_linkedlist=LinkedList(1)
    my_linkedlist.append(2)
    my_linkedlist.append(3)
    my_linkedlist.prepend(4)
    my_linkedlist.append(6)
    my_linkedlist.prepend(5)
    print(my_linkedlist)
    print(my_linkedlist.length)
    
    my_linkedlist.insert(4,11)
    print(my_linkedlist.search(4))
    print(my_linkedlist.get(4))
    print(my_linkedlist)
    my_linkedlist.set_value(2,26)
    print(my_linkedlist)
    my_linkedlist.pop_first()
    print(my_linkedlist)
    my_linkedlist.pop()
    print(my_linkedlist)
    my_linkedlist.remove(2)
    print(my_linkedlist)
