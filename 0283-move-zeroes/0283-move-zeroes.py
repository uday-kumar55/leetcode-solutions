class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        output = []
        for i in range(0,n):
            if nums[i] !=0:
                output.append(nums[i])
        while len(output) < n:
            output.append(0)
        for i in range(0,n):
            nums[i] = output[i]