from typing import List
class Solution:
    def hasSolution(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen: return True
            seen.add(n)
        return False 

print(Solution().hasSolution([1, 2, 3, 5]))