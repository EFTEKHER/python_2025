from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x=[]
        nums.sort()
       
        if len(nums)==0:
            return []
        last=len(nums)-2
        first=0
     
        sum=0
        for i in range(len(nums)):
            a=nums[i]
            new_nums=nums[:i]+nums[i+1:]
            if len(nums)==0:
                continue
            while(first<last):
                sums=a+new_nums[first]+new_nums[last]
                
                if sums>0:
                    last -=1
                elif sums<0:
                    first+=1
                else:
                    x.append([a,new_nums[first],new_nums[last]])
                    while(first<last and new_nums[first]==new_nums[first+1]):
                        first+=1
                    while(first<last and new_nums[last]==new_nums[last-1]):
                        last-=1
                    first+=1
                    last-=1
        return x            




if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))