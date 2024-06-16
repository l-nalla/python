arr = [2,5,1,3]
target = 4

from typing import List
class Solution:
    def twosum(self, arr : List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(arr):
            diff = target - n

            if diff in hm:
                return [hm[diff], i]
            hm[n] = i
        return

print(Solution().twosum(arr, target))