class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_ = nums[0]
        for i in nums:
            if min_ > i:
                min_ = i
        return min_