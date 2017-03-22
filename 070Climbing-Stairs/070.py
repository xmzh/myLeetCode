#法2

class Solution(object):
    
    def climbStairs(self, n):
        import numpy as np
        """
        :type n: int
        :rtype: int
        """
    
        memo= np.zeros(n+1,np.int32)
        return climb_Stairs(0, n, memo)

def climb_Stairs(i,n,memo):
    if i > n:
        return 0
    if i == n:
        return 1
    if memo[i] > 0:
        return memo[i]
    memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo)
    return memo[i]
        

#法3
class Solution(object):
    
    def climbStairs(self, n):
        import numpy as np
        """
        :type n: int
        :rtype: int
        """
    
        if n == 1:
            return 1

        dp = np.zeros(n+1,np.int32)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

