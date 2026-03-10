# 3130. Number of Stable Arrays

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] -> arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] -> arrays with i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases initialization
        # A sequence of only 0s is valid as long as its length is <= limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
            
        # A sequence of only 1s is valid as long as its length is <= limit
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        # Fill the DP table
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                
                # 1. Calculate combinations ending in 0
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                if i > limit:
                    # Subtract cases where appending 0 creates limit + 1 consecutive 0s
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD
                    
                # 2. Calculate combinations ending in 1
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                if j > limit:
                    # Subtract cases where appending 1 creates limit + 1 consecutive 1s
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD
                    
        # The total valid arrays will be the sum of arrays ending in 0 and arrays ending in 1
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD