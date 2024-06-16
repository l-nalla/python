from typing import List
class Solution:
    def groupanagrams(self, anagrams: List[str]) -> List[List[str]]:
        hm = {}

        for s in anagrams:
            ss = "".join(sorted(s))
            
            if ss in hm:
                hm[ss].append(s)
            else:
                hm[ss] = [s]
            
        return [ val for val in hm.values()]

print(Solution().groupanagrams(['eat','tea','tan','ate','nat', 'bat']))
