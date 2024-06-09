class Solution:

    def vowel_cosonents(self, string : str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vo = 0
        consonents = 0
        for s in string:
            if s.isalpha() and s not in vowels:
                consonents += 1
            elif s.isalpha() and s in vowels:
                vo += 1
        return {"vowels": vo, "consonents": consonents }

print(Solution().vowel_cosonents("this. "))