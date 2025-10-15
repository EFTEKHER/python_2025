from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0, len(height)-1
        area=0
        while left<right:
            h=min(height[left],height[right])
            w=right-left
            new_area=h*w
            area=max(area,new_area)
            
            if height[left]<height[right]:
                left+=1
            else:
                right -=1
        return area
    
                