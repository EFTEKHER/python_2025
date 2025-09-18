
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         if len(nums)==0:
             return 0
         x=[]
         nums.sort()
         for i in range(len(nums)-1):
             if((nums[i]!=nums[i+1])):
                 x.append(nums[i])
         x.append(nums[-1])
         nums=x
         
         return len(nums)
     
     
if __name__ == "__main__":
    s=Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))                      
             
  