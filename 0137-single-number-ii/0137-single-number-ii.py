class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = {}
        output = []
        for i in range(0,len(nums)):
            ch = nums[i]
            f[ch] = f.get(ch,0)+1
        for key in f:
            if f[key] == 1:
                return key