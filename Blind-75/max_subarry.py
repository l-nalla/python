arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

from typing import List
class Solution:
    def max_subarray(self, arr: List[int]) -> int:
        maxSub = arr[0]
        curSum = 0

        for i in arr:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSubArr = max(maxSub, curSum)
        return maxSubArr

print(Solution().max_subarray(arr))