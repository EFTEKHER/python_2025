### possible all unique 4 set combination from list
from typing import List
class Solution:
     ##combination buit in library iteratools
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        from itertools import combinations
        x=combinations(nums,4)
        y=set(x)
        x=list(x)
        return x
if __name__=="__main__":
    s=Solution()
    print(s.fourSum([1,0,-1,0,-2,2],0))
    print(s.fourSum([2,2,2,2,2],8))