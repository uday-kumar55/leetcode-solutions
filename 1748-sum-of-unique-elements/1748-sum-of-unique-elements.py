class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = {}
        output = 0
        for i in range(0,len(nums)):
            ch = nums[i]
            f[ch] = f.get(ch,0)+1
        for key in f:
            if f[key] == 1:
                output = output + int(key)
        return output