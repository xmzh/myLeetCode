class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        import numpy as np
        maxans = 0
        dp=[]
        for  i in range(1,len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i>=2:
                        dp[i] =  dp[i - 2] + 2
                    else:
                        dp[i] =  2
                else:
                    if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                        if i - dp[i - 1] >= 2:
                            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2]  + 2
                        else:
                            dp[i] = dp[i - 1] + 2
                
                maxans = max(maxans, dp[i])

        return maxans
