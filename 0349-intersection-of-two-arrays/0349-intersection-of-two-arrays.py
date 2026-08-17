class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr = []
        i = 0
        while i<len(nums2):
            if nums2[i] in nums1 and  nums2[i] not in arr:
                arr.append(nums2[i])
            i+=1
        return arr