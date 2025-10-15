
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        ui=True
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ui=False
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
if __name__=="__main__":
    s=Solution()
    print(s.searchInsert([1,3,5,6],2)) 
    print(s.searchInsert([1,3,5,6],4))
    print(s.searchInsert([1,3,5,6],5))
    print(s.searchInsert([1,3,5,6],7))
    print(s.searchInsert([1,3,5,6],0))
           
            
        