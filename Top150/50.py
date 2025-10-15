class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        y=x[::-1]
        return x==y
    
if __name__=="__main__":
    s=Solution()
    print(s.isPalindrome(-121))