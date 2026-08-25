class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a = ""
        i =0
        j = 0
        while i <len(word1) and j<len(word2):
            a = a+word1[i] + word2[j]
            i=i+1
            j=j+1
        while i <len(word1):
            a = a+word1[i]
            i=i+1
        while j <len(word2):
            a = a+ word2[j]
            j=j+1
        return a