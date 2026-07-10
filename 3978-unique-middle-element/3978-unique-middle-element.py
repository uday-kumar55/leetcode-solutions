class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)//2
        mid = nums[n]
        for i in range(0,len(nums)):
            if i !=n and mid ==nums[i]:
                return False
        return True