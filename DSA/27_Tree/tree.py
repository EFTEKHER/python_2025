class Tree1:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
    def __str__(self, level=0):
        s=" "*level+str(self.data)+"\n"
        for child in self.children:
            s+=child.__str__(level+1)
        return s
    def addChild(self,Tree1):
        self.children.append(Tree1)
drinks=Tree1('Drinks',[])
Hot=Tree1('Hot',[])
cold=Tree1('cold',[])
drinks.addChild(Hot)
drinks.addChild(cold)
print(drinks)        
            