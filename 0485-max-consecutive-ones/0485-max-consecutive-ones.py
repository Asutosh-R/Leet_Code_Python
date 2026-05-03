class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        best = 0

        for num in nums:
            if num == 1:
                count = count + 1
                if count > best:
                    best = count
            else:
                count = 0

        return best
                
        


        