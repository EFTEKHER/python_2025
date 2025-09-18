from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p            
            else:
                best = max(best, p - min_price)  
        return best

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:        
                
                
                
                
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    s=Solution()
    print(s.maxProfit(prices))
    prices = [7,6,4,3,1]
    print(s.maxProfit(prices))                
        