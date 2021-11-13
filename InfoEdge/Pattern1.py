class Solution:
    def pattern(self, n):

        for i in range(n, 0, -1):
            print(int('1'*i)**2)


obj = Solution()
obj.pattern(10)
