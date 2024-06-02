arr = [1,2,3,1]

class Solution:
    def robmax(self, arr):
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for n in arr:
            temp = max(rob1+n, rob2) # robbing completed
            rob1 = rob2
            rob2 = temp
        return rob2

print(Solution().robmax(arr))