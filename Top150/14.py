# for 1,2,3 we get 1 
# for 4,5,6,7,8 we  get 2
# for  9,10,11,12,13,14,15 we get 3
# for 16 to 24 we get 4
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            curr = mid * (mid + 1) // 2
            if curr == n:
                return mid
            if curr < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
if __name__=="__main__":
    s=Solution()
    print(s.arrangeCoins(5)) 
    print(s.arrangeCoins(8))
    print(s.arrangeCoins(1))
    print(s.arrangeCoins(2))
    print(s.arrangeCoins(3))
    print(s.arrangeCoins(6))
    print(s.arrangeCoins(7))
    print(s.arrangeCoins(10))
    print(s.arrangeCoins(11))
    print(s.arrangeCoins(12))
    print(s.arrangeCoins(13))
    print(s.arrangeCoins(14))
    print(s.arrangeCoins(15))
    print(s.arrangeCoins(16))
    print(s.arrangeCoins(17))
    print(s.arrangeCoins(18))
    print(s.arrangeCoins(19))
    print(s.arrangeCoins(20))
    print(s.arrangeCoins(21))
    print(s.arrangeCoins(22))
    print(s.arrangeCoins(23))
    print(s.arrangeCoins(24))    