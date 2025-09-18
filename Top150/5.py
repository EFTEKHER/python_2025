from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_count={}
        majortity_element=len(nums)//2
        for i in nums:
            ##count frequency of each element in the lst nums as key, frequency as total occurences
            if i in dict_count:
                dict_count[i]+=1
            else:
                dict_count[i]=1
        for key, value in dict_count.items():
            if value >= majortity_element:
                return key
        return -1
    
if __name__ == "__main__":
    l1=[3,2,3]
    s=Solution()
    print(s.majorityElement(l1))
    l2=[2,2,1,1,1,2,2]
    print(s.majorityElement(l2))    
