nums = [2,7,11,15]
target = 9

class Solution:
    def twosumtwo(self, arr, trg):
        l, r = 0, len(arr) - 1

        while l < r:
            curSum = arr[l] + arr[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []

print(Solution().twosumtwo(nums, target))