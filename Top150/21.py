from collections import deque
from typing import List, Tuple

class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        # store the input midway (as requested)
        donquarist: Tuple[Tuple[int, ...], Tuple[int, ...]] = (tuple(nums1), tuple(nums2))

        start = tuple(nums1)
        target = tuple(nums2)
        if start == target:
            return 0

        # BFS over states (arrays as tuples)
        q = deque([(start, 0)])
        seen = {start}

        while q:
            arr, d = q.popleft()
            n = len(arr)

            # try all cut-and-paste operations
            for L in range(n):
                for R in range(L, n):
                    seg = arr[L:R+1]
                    rest = arr[:L] + arr[R+1:]

                    # insert seg into any gap in 'rest'
                    for p in range(len(rest) + 1):
                        new_arr = rest[:p] + seg + rest[p:]
                        if new_arr == arr:      # no-op (same place)
                            continue
                        if new_arr in seen:
                            continue
                        if new_arr == target:
                            return d + 1
                        seen.add(new_arr)
                        q.append((new_arr, d + 1))

        # Should never hit here (nums2 is a permutation of nums1)
        return -1


# Quick tests from the prompt
if __name__ == "__main__":
    s = Solution()
    print(s.minSplitMergeOps([3,1,2], [1,2,3]))                 # 1
    print(s.minSplitMergeOps([1,1,2,3,4,5], [5,4,3,2,1,1]))     # 3
    print(s.minSplitMergeOps([1,2], [2,1]))                     # 1
