class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        sum = 0
        max = 0
        for i in range(0,len(gain)):
            sum = sum+gain[i]
            if(sum>max):
                max = sum
        return max