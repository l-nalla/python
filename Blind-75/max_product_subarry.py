arr = [2,3,-2,4]

from typing import List

class Solution:
    def max_product_subarr(self, arr: List[int]) -> int:
        res = max(arr)
        curMin, curMax = 1, 1

        for n in arr:
            if n == 0:
                curMin, curMax = 1, 1
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax, curMin)
        return res

print(Solution().max_product_subarr(arr))

