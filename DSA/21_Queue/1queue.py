class Queue:
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.top=-1
        self.start=-1
        self.lists=['None']*maxSize
    def isFull(self):
        if self.start==0 and self.top+1==self.maxSize:
            return True
        if self.top+1==self.start:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def __str__(self):
        result=[str(x) for x in self.lists]
        return ' '.join(result)    
    def enqueue(self,value):
        if self.isFull():
            return 'out of bound' 
        else:
            self.top +=1
            if self.start ==-1:
                self.start=0
            if self.top+1==self.maxSize:
                self.top=0    
            self.lists[self.top]=value
            return 'value is inserted'
    def dequeue(self):
        if self.isEmpty():
            return 'it is empty'
        if self.start+1==self.maxSize:
            self.start=0
        if self.start==self.top:
            x=self.lists[self.start]
            self.lists[self.start]='None'
            self.start=-1
            self.top=-1
            return x    
        else:
            x=self.lists[self.start]
            self.lists[self.start]='None'
            self.start+=1
            return x

if __name__ == "__main__":
    que=Queue(5)
    print(que.isEmpty())
    print(que.isFull())
    que.enqueue(4)
    que.enqueue(5)
    que.enqueue(6)
    que.enqueue(7)
    que.enqueue(8)
    print(que)
    print(que.dequeue())
    print(que.dequeue())
    que.enqueue(9)
    que.enqueue(10)
    
    print(que)
        
        