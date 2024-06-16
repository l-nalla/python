arr = [7, 1, 4, 3, 6, 4]

from typing import List
class Solution:
    def besttimetobuysell(self, arr: List[int]) -> int:
        curMin = arr[0]
        curMax = arr[0]

        for i in arr:
            if i < curMin:
                curMin = i
                curMax = i
            
            if i > curMax:
                curMax = i
            
        return curMax - curMin
    
print(Solution().besttimetobuysell(arr))
