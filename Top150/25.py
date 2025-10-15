from typing import List
class Solution:
     
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        x=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for  j in range(i+1,len(nums)):
                if j>i+1 and  nums[j]==nums[j-1]:
                    continue
                start,last=j+1,len(nums)-1
                while(start<last):
                    sum=nums[j]+nums[start]+nums[last]+nums[i]
                    
                    if sum>target:
                        last-=1
                    elif sum<target:
                        start +=1
                    else:
                         x.append([nums[i],nums[j],nums[start],nums[last]])
                         while start<last and nums[start+1]==nums[start]:
                             start+=1
                         while start<last and nums[last-1]==nums[last]:
                             last-=1 
                         start+=1
                         last-=1
        nums[:]=x
        return nums  
    
                             