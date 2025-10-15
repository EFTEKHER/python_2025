class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""



# Example 5:

# Input: s = "([)]"

# Output: false
if __name__ == "__main__":
    s = Solution()
            # False
    print(s.isValid("([)]"))        # False
    print(s.isValid("{[]}"))        # True