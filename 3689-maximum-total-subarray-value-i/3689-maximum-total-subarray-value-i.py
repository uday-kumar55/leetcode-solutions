class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxs = nums[0]
        mins =nums[0]
        for i in range(len(nums)):
            if(maxs<nums[i]):
                maxs = nums[i]
            if(mins>nums[i]):
                mins =nums[i]
        sums =maxs -mins
        return sums*k