class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        ##h-index must be smaller or equal to the number of paper published
        ##sorted in increasing order
        ##at i, there will be n-i publish having at least citation[i] citations
        ##h = min(n-i, citations[i])
        citations.sort()
        length = len(citations)
        h = 0
        for i in range(length):
            citation = citations[i]
            temp = min(citation, length-i)
            if h < temp:
                h = temp
        return h