# group anagrams together
from collections import defaultdict
class Solution:
    def groupanagrams(self, strs):
        anagram_group = {}


        for s in strs:
            ss = "".join(sorted(s))
            if ss in anagram_group:
                anagram_group[ss].append(s)
            else:    
                anagram_group[ss] = [s]
        
        return [val for val in anagram_group.values()]



print(Solution().groupanagrams(['eat','tea','tan','ate','nat', 'bat']))