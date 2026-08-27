class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = nums[0]
        sum1 = nums[0]
        for i in range(1,len(nums)):
            sum1 = sum1 + nums[i]
            if sum1 < nums[i]:
                sum1 = nums[i]
            if max1 < sum1:
                max1 = sum1
        return max1