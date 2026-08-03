class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_ = nums[0]
        for i in range(0,len(nums)):
            if min_>nums[i]:
                min_ = nums[i]
        return min_