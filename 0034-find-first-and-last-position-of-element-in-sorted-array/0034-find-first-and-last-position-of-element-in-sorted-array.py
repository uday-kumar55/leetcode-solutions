class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(0,len(nums)):
            if nums[i] == target:
                output.append(i)
        if len(output) == 0:
            return [-1,-1]
        return [output[0],output[len(output)-1]]