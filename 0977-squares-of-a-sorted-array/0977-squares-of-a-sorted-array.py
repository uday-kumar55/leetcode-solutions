class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i =0
        j =len(nums)-1
        arr = [0]*len(nums)
        k = len(nums)-1
        while i<=j:
            sum1 = nums[i]**2
            sum2 = nums[j]**2
            if sum1<sum2:
                arr[k] = sum2
                j-=1
            else:
                arr[k] = sum1
                i+=1
            k-=1
        return arr


          