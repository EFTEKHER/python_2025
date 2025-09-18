

from typing import List
class Solution:   
     rows=[]
     mini=0
     def earliestTime(self, tasks: List[List[int]]) -> int:
        ## sum row wise for each  row in 2d list and store it in a list
        rows=[sum(i) for i in tasks]
        mini=min(rows)
        return mini
if __name__ == "__main__":
    #     `Example 1:

    # Input: tasks = [[1,6],[2,3]]

    # Output: 5

    # Explanation:

    # The first task starts at time t = 1 and finishes at time 1 + 6 = 7. The second task finishes at time 2 + 3 = 5. You can finish one task at time 5.

    # Example 2:

    # Input: tasks = [[100,100],[100,100],[100,100]]

    # Output: 200

    # Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
        
        tasks = [[1,6],[2,3]]
        s=Solution()
        print(s.earliestTime(tasks))
        tasks = [[100,100],[100,100],[100,100]]         
        print(s.earliestTime(tasks))
        
        
        
        
        
        