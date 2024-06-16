arr = [1,2,3,1]
arr1 = [1,2,3,4]

from typing import List
class Solution:
    def contains_duplicates(self, arr: List[int]) -> bool:
        hs = set()

        for i in arr:
            if i in hs:
                return True
            hs.add(i)
        return False

print(Solution().contains_duplicates(arr))
print(Solution().contains_duplicates(arr1))