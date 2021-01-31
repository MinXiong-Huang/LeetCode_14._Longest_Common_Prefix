class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        s1 = min(strs)
        s2 = max(strs)

        for i,j in enumerate(s1):
            if j not in s2[i]:
                return s1[:i]
        return s1    

#Example
s = Solution()
s.longestCommonPrefix(["flower","flow","flight"])
