#法1
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if (nums[j] != val):
                nums[i] = nums[j]
                i=i+1
        return i

#法2
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        while (i < n):
            if (nums[i] == val):
                nums[i] = nums[n - 1]
                n=n-1
            else:
                i=i+1
        return n
