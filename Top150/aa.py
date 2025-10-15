from typing import List

class Solution: 
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        nums.sort()
        sormadexin = nums[:]
        
        max_val = max(sormadexin)
        min_val = min(sormadexin)
        diff = max_val - min_val
        
        if diff == 0:
            return 0
        if len(nums) == k:
            return diff
        return diff * k


if __name__ == "__main__":
    s = Solution()
    
    # Input: nums = [11, 8], k = 2
    print(s.maxTotalValue([11, 8], 2))  
    
    # Input: nums = [4, 2, 5, 1], k = 3
    print(s.maxTotalValue([4, 2, 5, 1], 3))
    
    # Input: nums = [1, 3, 2], k = 2
    print(s.maxTotalValue([1, 3, 2], 2))
    
    # Input: nums = [1, 1, 1, 1], k = 2
    print(s.maxTotalValue([1, 1, 1, 1], 2))
