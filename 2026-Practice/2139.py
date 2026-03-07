# Example 1:

# Input: target = 5, maxDoubles = 0
# Output: 4
# Explanation: Keep incrementing by 1 until you reach target.
# Example 2:

# Input: target = 19, maxDoubles = 2
# Output: 7
# Explanation: Initially, x = 1
# Increment 3 times so x = 4
# Double once so x = 8
# Increment once so x = 9
# Double again so x = 18
# Increment once so x = 19
# Example 3:

# Input: target = 10, maxDoubles = 4
# Output: 4
# Explanation: Initially, x = 1
# Increment once so x = 2
# Double once so x = 4
# Increment once so x = 5
# Double again so x = 10
 

# Constraints:

# 1 <= target <= 109
# 0 <= maxDoubles <= 100





class Solution(object):
    def minMoves(self, target, maxDoubles):
        steps = 0
        
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            steps += 1
        
        # If no doubles left, just subtract remaining in one go
        if target > 1:
            steps += (target - 1)
       
        return steps