from typing import List
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = list(map(int, version1.split(".")))
        list2 = list(map(int, version2.split(".")))

        n1, n2 = len(list1), len(list2)
        
        m = max(n1, n2)

        for i in range(m):
            v1 = list1[i] if i < n1 else 0
            v2 = list2[i] if i < n2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0          
            
if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion("1.01","1.001")) 
    print(s.compareVersion("1.0","1.0.0"))
    print(s.compareVersion("0.1","1.1"))
    print(s.compareVersion("1.0.1","1"))
    # Input: version1 = "1.0", version2 = "1.0.0.0"
    print(s.compareVersion("1.0","1.0.0.0"))
    # Input: version1 = "1.2", version2 = "1.10"
    print(s.compareVersion("2.2","1.10"))
# 165. Compare Version Numbers
     
    
#     Example 1:

# Input: version1 = "1.2", version2 = "1.10"

# Output: -1

# Explanation:

# version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

# Example 2:

# Input: version1 = "1.01", version2 = "1.001"

# Output: 0

# Explanation:

# Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

# Example 3:

# Input: version1 = "1.0", version2 = "1.0.0.0"

# Output: 0

# Explanation:

# version1 has less revisions, which means every missing revision are treated as "0".


 
           
        