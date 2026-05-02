class Solution(object):
    def shuffle(self, nums, n):
        c=[]
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        a= nums[:n]
        b= nums[n:]
            
        for i,j in zip(a,b):
            c.append(i)
            c.append(j)
        return c

        