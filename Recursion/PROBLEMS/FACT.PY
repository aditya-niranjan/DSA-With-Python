class Solution:
    def fact(self,n):
        if n == 1 or n == 0:
            return 1
        return n * self.fact(n-1)
    

instanceOne = Solution()
instanceTwo = Solution()

print(instanceOne.fact(5))
print(instanceTwo.fact(10))
