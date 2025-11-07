# this is nothing but addtion of the sum of all numbers Using the Functional Recursion

class Solution:
    def func(self,n):
        if n == 1:
            return 1

        return n+self.func(n-1)
    

s1 = Solution()
s2 = Solution()
s3 = Solution()
print(s1.func(10))
print(s2.func(50))
print(s3.func(100))
