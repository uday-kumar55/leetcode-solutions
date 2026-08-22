class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum1 = 0
        sum2 = 1
        m = n
        while n>0:
            digit = n%10
            sum1 = sum1 + digit
            sum2 = sum2*digit
            n = n//10
        output = sum1+sum2
        return m%output ==0