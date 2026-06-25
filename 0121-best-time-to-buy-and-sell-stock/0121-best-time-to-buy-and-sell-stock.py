class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_1 = prices[0]
        max_1 = 0
        for i in range(len(prices)):
         if min_1>prices[i]:
            min_1 = prices[i]
         pricess = prices[i] - min_1
         if pricess>max_1 :
            max_1 = pricess
        
        return max_1
