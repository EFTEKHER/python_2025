from typing import List, Dict
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x={}
        li=[]
        for i in range(len(nums)):
            if nums[i] in x:
                x[nums[i]]+=1
            else:
                x[nums[i]]=1
            
        # If x value is more than  2 or equal to 2 then we will not append it to the list twice
        for i in x:
            if x[i]>=val:
                li.append(i)
                li.append(i)
            else:
                li.append(i)
            
        nums[:]=li
        del x
        del li
        return len(nums)
    
 
if __name__ == "__main__":
    l1=[1,1,1,2,2,3]
    val=2
    s=Solution()
    print(s.removeElement(l1,val)) 
    # Input: nums = [0,0,1,1,1,1,2,3,3]
    #  t: 7, nums = [0,0,1,1,2,3,3,_,_] 
    l2=[0,0,1,1,1,1,2,3,3]
    val=2
    s=Solution()
    print(s.removeElement(l2,val))