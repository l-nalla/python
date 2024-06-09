class Solution:

    def long_substr(self, string: str) -> str:
        substr = ""
        for s in string:
            if s not in substr:
                substr += s
            else:
                return substr
        return
    
print(Solution().long_substr("abcdaabc"))