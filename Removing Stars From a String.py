class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## every time read the stars, check the current largest available non-star index
        ## output the rest of the available
        string = list(s)
        avail, result = [], []
        for i in range(len(s)):
            if string[i] == "*":
                ## now we remove the leftmost
                current = avail[-1] ## it must exist
                avail.pop(-1)
            else:
                avail.append(i)
        for i in range(len(avail)):
            result.append(string[avail[i]])
        if result == []: return ""
        else: return "".join(result)