def mRR(l1,m,l2,n):
    x=[]
    for i in range(m):
        x.append(l1[i])
    for j in range(n):
        x.append(l2[j])  
        
        
    x.sort()
    return x
  
#   Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
if __name__ == "__main__":
    l1=[1,2,3,0,0,0]
    m=3
    l2=[2,5,6]
    n=3
    print(mRR(l1,m,l2,n))