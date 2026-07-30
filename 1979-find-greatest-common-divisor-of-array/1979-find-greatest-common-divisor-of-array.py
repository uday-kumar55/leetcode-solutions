
class Solution(object):
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = nums[0]
        min_ = nums[0]
        for i in range(0,len(nums)):
            if max_< nums[i]:
                max_ =nums[i]
            if min_ > nums[i]:
                min_= nums[i]
        return self.gcd(min_,max_)