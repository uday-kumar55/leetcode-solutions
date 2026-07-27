class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        max2 = 0
        for i in range(0,len(nums)):
            if max1 <nums[i]:
                max2 = max1
                max1 = nums[i]
            elif max2<nums[i]:
                max2 = nums[i]
        sum_ = (max1 -1)*(max2-1)
        return sum_
