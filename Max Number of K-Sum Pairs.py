class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ## for each number there will only be on corresponding that forms a pair
        ## if we brutely look up for each character that will be O(N^2) which is inefficient
        ## i to scan the list
        ## j to record the index of each character looking up
        lookup = {}
        counter = 0
        for num in nums:
            if k <= num:
                continue
            elif num in lookup and lookup[num] > 0:
                counter += 1
                lookup[num] -= 1
            else:
                if k-num not in lookup:
                    lookup[k-num] = 1
                else:
                    lookup[k-num] += 1
        return counter