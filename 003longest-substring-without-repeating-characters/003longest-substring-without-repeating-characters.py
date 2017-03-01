#法1
def allUnique(s,start,end):
        a=set()
        for i in range(start,end):
            ch = s[i]
            if (ch in a):
                return False
            a.add(ch)
        return True


class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i+1,n+1):
                if (allUnique(s, i, j)):
                    ans = max(ans, j - i)
        return ans


#法2
class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        a=set()
        ans = 0
        i=0
        j=0
        while i<n and j<n:
            if((s[j] not in a)):
                a.add(s[j])
                j+=1
                ans = max(ans, j - i)
            else:
                a.remove(s[i])
                i+=1
        return ans
#法3
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        amap={}
        ans = 0
        i=0
        for j in range(n):
            if amap.get(s[j],0)!=0:
                i=max(amap[s[j]],i)
            ans = max(ans, j - i + 1)
            amap[s[j]]=j+1
        return ans
    
#法4    
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
