from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        l1=
        Do not return anything, modify nums in-place instead.
        """
        l1=[]
        l2=[]
        n=len(nums)
        k=k%n
        l2=nums[-k:]
        l1=nums[:-k]
        nums[:]=l2+l1
        return nums
    
    
#   Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
if  __name__ == "__main__":
    l1=[1,2,3,4,5,6,7]
    k=3
    s=Solution()
    print(s.rotate(l1,k))
    l2=[-1,-100,3,99]
    k=2
    print(s.rotate(l2,k))
    l3=[1,2,3]  
    k=0
    print(s.rotate(l3,k))

# Input
# nums =
# [1,2,3]
# k =
# 0

# Use Testcase
# Output
# [2,3,1]
# Expected
# [1,2,3]
    