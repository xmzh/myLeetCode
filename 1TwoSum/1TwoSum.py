class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for ind, val in enumerate(nums):
            hash_map[val] = ind

        for ind1, val in enumerate(nums):
	    compent = target-val
            if compent in hash_map:
                ind2 = hash_map[compent]
                if ind1!=ind2:
                    return ind1, ind2

if __name__=="__main__":
    print Solution().twoSum([3, 2, 4], 6)