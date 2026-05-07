class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        l= []
        ma = max(target)
        for i in range(1,n+1):
            if i < ma+1:
                l.append("Push")
                if i not in target:
                    l.append("Pop")
            else:
                break
                 
        return l 