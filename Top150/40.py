from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(2,len(nums)):
            if nums[i-1]+nums[i-2]>nums[i]:
                count=nums[i]+nums[i-1]+nums[i-2]
                
           
        return count             
                
if __name__=="__main__":
    s=Solution()
    print(s.largestPerimeter([2,1,2]))
    print(s.largestPerimeter([1,2,1,10]))        