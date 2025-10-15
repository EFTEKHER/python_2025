class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1        
if __name__ == "__main__":
    s=Solution()
    print(s.strStr("hello","ll"))
    print(s.strStr("aaaaa","bba"))                 
        