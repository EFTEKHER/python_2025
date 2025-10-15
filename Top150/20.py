
from typing import List
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        sum=0
        count=0
        x=True
        for i in range(len(nums)):
            if(nums[i]%2==0):
                sum |=nums[i]
                               
            else:
                count+=1
                x=False    
        if len(nums)==count and x:
            return 0
        elif len(nums)==1 and nums[0]%2==0:
            return nums[0]
        else:
            return sum
if __name__=="__main__":
    s=Solution()
    print(s.evenNumberBitwiseORs([12,9,8]))
    print(s.evenNumberBitwiseORs([3,5,7])) 
# You are given a 0-indexed integer array nums. The bitwise OR of a subarray is the bitwise OR of all the elements in it.
    print(s.evenNumberBitwiseORs([1,2,3,4,5,6]))
    print(s.evenNumberBitwiseORs([7,9,11]))
    print(s.evenNumberBitwiseORs([1,8,16]))
    print (s.evenNumberBitwiseORs([2]))
    
#     Example 1:

# Input: nums = [1,2,3,4,5,6]

# Output: 6

# Explanation:

# The even numbers are 2, 4, and 6. Their bitwise OR equals 6.

# Example 2:

# Input: nums = [7,9,11]

# Output: 0

# Explanation:

# There are no even numbers, so the result is 0.

# Example 3:

# Input: nums = [1,8,16]

# Output: 24

# Explanation:

# The even numbers are 8 and 16. Their bitwise OR equals 24.©leetcode       
    
                