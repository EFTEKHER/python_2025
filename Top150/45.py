from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a=nums[1]
        
        if nums[0]==0:
            return False
        i=1
        x=a+i
        k=True
        for i in range(1,x):
            if nums[i]==0:
                k=False
        if x==(len(nums)-1) and k:
            return True
        else:
            return False

if __name__=="__main__":
    s=Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
                    
            
        
            