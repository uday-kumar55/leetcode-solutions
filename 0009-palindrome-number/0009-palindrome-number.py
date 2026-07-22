class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        real = x
        if x <0:
            return False
        reverse = 0
        while x>0:
            sum_ = x%10
            reverse = reverse*10+sum_
            x = x//10
        return real==reverse

        