class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = nums[0]
        for i in range(len(nums)):
            if maxs<nums[i]:
                maxs = nums[i]
        for i in range(len(nums)):
            if maxs ==nums[i]:
                return i