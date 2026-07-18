from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_ = nums[0]
        min_ = nums[0]
        for i in range(0,len(nums)):
            if max_< nums[i]:
                max_ =nums[i]
            if min_ > nums[i]:
                min_= nums[i]
        return gcd(min_,max_)
        