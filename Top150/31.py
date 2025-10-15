from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
       
        # Fix the largest side
        for k in range(n - 1, 1, -1):
            left, right = 0, k - 1
            print(f"left={left}, right={right}, k={k}")
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    # Instead of count += (right - left)
                    # loop and do count += 1 for each
                    for i in range(left, right):
                        count += 1
                    right -= 1
                else:
                    left += 1
                print(f"left={left}, right={right}, k={k}, count={count}")    
        return count
if __name__=="__main__":
    s=Solution()
    print(s.triangleNumber([2,2,3,4]))                      
    # print(s.triangleNumber([4,2,3,4]))
    # print(s.triangleNumber([0,1,1,1]))