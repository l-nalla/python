class Solution:
    def ispalindrome(self, string: str) -> bool:
        new_str = ""

        for s in string.lower():
            if s.isalpha():
                new_str += s

        return new_str == new_str[::-1]


print(Solution().ispalindrome("step on, no pets"))