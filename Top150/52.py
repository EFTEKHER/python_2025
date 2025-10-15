from typing import List
class Solution:
    def maxBottlesDrunk(self,numBottles: int, numExchange: int) -> int:
            empty=0
            drink=0
            empty+=numBottles
            drink+=numBottles
            while empty>=numExchange:
                empty-=numExchange
                numExchange+=1
                drink+=1
                empty+=1
            return drink
if __name__=="__main__":
    s=Solution()   
    print(s.maxBottlesDrunk(9,3))
        
        