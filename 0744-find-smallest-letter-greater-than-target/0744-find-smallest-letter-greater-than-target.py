class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        for i in range(n):
            if letters[i] > target:
                return letters[i]
        return letters[0]