
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x=[]
        for i in nums:
            if i==val:
                continue
            else:
                x.append(i)
        nums=x  
        
        return len(nums), nums 
    
if __name__ == "__main__":
    l1=[3,2,2,3]
    val=3
    s=Solution()
    print(s.removeElement(l1,val))