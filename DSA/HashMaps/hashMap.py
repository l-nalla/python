#TwoSum problem

arr = [2,1,5,3]

class Solution:
    def twoSum(self, arr, key):
        prevMap = {}
        for i, n in enumerate(arr):
            diff = key - n
            if diff in prevMap:
                return (prevMap[diff], i )
            prevMap[n] = i
        return 

print(Solution().twoSum(arr, 4))