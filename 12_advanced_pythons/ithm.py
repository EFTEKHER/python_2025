# def maxsubary(nums):
#     csum=0
#     msum=float('-inf')
#     for i in nums:
#         csum+=i
#         msum=max(msum,csum)
#         if csum<0:
#             csum=0
#     return msum


# if __name__ == "__main__":
#     print(maxsubary([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
#     print(maxsubary([1]))                        # Output: 1
#     print(maxsubary([5,4,-1,7,8]))               # Output: 23
#     print(maxsubary([-1,-2,-3]))                 # Output: -1
#     print(maxsubary([0,-3,5,-2,1,-1,2,-3,4]))    # Output: 7


# /*
# code written by Eftekher Ali Efte from Bangladesh 
# email: eftekherali2000@gmail.com
# pursuing computer science and engineering in RUET
# */

# def funct(x, i):
#     s = x[i]
#     if i > 0:
#         s += funct(x, i - 1)
#     print(s, end="")  # same as printf("%d", s) without spaces/newlines
#     return s


# def main():
#     y = [1, 3, 2, 8]
#     funct(y, 2)


# if __name__ == "__main__":
#     main()


def fun():
    a=1
    b=2
    c=3
    print(f"{a+=(a+=3,5,a)}")


