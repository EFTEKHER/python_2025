from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        efte=[]
        for i in range(numRows):
            efte.append([0]*(i+1))
            for j in range(i+1):
                if(j==0 or j==i):
                    efte[i][j]=1
                else:
                    efte[i][j]=efte[i-1][j-1]+efte[i-1][j]
        return efte                
if __name__=="__main__":
    s=Solution()
    print(s.generate(5))            
        