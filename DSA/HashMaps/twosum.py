from typing import List
class Solution:
    def twosum(self, nums: List[int], t: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            diff = t - n
            if diff in hm:
                return [hm[diff], i]
            hm[n] = i
        
print(Solution().twosum([2,7,11,15], 9))
