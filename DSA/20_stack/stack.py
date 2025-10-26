class stack:
    def __init__(self):
        self.list1=[]
    def __str__(self):
        # list.reverse() operates in-place and returns None — that's why
        # `z = self.list1.reverse()` was not iterable. Use reversed()
        # (returns an iterator) or slicing to get a reversed view.
        return '\n'.join(map(str, reversed(self.list1)))
    def is_empty(self):
        if self.list1 == []:
            return True
        else:
            return False
    def push(self, value):
        self.list1.append(value)
    def  pop (self):
        if self.is_empty():
            return 'Empty'
        else:
            self.list1.pop()
    def seek(self):
        if self.is_empty():
            return 'Empty'
        else:
            return self.list1[len(self.list1)-1]           
        
 
 
if __name__=='__main__':
    st=stack()
    st.push(4)
    st.push(5)
    st.push(6)
    st.push(7)
    st.push(9)
    print(st)
    print('----------------')
    st.pop()
    print(st) 
    print(st.seek())           
    