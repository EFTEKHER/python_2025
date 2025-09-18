
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        max_reach=0
        for i in range(n):
            if i>max_reach:
                return False
            max_reach=max(max_reach,i+nums[i])
        return True
if __name__=="__main__":
    nums = [2,3,1,1,4]
    s=Solution()
    print(s.canJump(nums))
    nums = [3,2,1,0,4]
    print(s.canJump(nums))
    nums = [0]
    print(s.canJump(nums))    