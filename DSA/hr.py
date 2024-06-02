class Solution:
    def __init__(self, length):
        self.n, self.m = length[0], length[1]
        
    def get_sets(self, length):
        s = set()
        count = 0
        while count < int(length):
            s.add(int(input()))
            count += 1 
        return s
        
    def check_happiness(self):
        A = self.get_sets(self.n)
        B = self.get_sets(self.m)
        val_n, val_m = input().split(" ")
        print(val_n, val_m)
        
        
if __name__ == "__main__":
    length = input()
    print(length)
    s = Solution(length)
    s.check_happiness()