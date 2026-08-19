class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        for i in range(0,len(nums)+1):
            output = output ^ i 
        for i in nums:
            output = output ^ i
        return output  