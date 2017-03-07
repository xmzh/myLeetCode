#法1
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0):
            return "";
        prefix = strs[0]
        for i in range(1,len(strs)):
            while (strs[i].find(prefix) != 0): #要从头开始一样
                prefix = prefix[0:len(prefix)-1]  #不一样，公共前缀去掉一个字符
                if (prefix==None):
                    return ""
        return prefix

#法2
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if (len(strs)== 0):
            return ""
        for i,c in enumerate(list(strs[0])): #对第一个字符串的每一个字符
            for k in range(1,len(strs)): #看看其余字符串的相同位置的字符是不是也是这个
                if (i == len(strs[k]) or strs[k][i:i+1] != c):
                    return strs[0][0:i]             

        return strs[0]

#法3
def commonPrefix(left,right):
    smin = min(len(left), len(right))  
    for i in range(smin):
        if ( left[i:i+1] != right[i:i+1] ):
            return left[0:i]
    return left[0:smin]
    
def longestCommonPrefix1(strs, l,r):
    if (l == r):
        return strs[l]
    else:
        mid = (l + r)/2
        lcpLeft =   longestCommonPrefix1(strs, l , mid)
        lcpRight =  longestCommonPrefix1(strs, mid + 1,r)
        return commonPrefix(lcpLeft, lcpRight)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (strs == None or len(strs) == 0):
            return ""
        return longestCommonPrefix1(strs, 0 , len(strs) - 1)

