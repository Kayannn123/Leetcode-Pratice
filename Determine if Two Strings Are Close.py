class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2): return False
        elif set(word1) != set(word2): return False
        counter, appearance = True, True
        word1, word2 = list(word1), list(word2)
        word1.sort() ##O(N log N)
        word2.sort()
        if word1 == word2: return True ## O(N)
        dict1, dict2 = {}, {}
        for i in range (len(word1)):
            char1 = word1[i]
            char2 = word2[i]
            if char1 not in dict1:
                dict1[char1] = 1
            else: dict1[char1] += 1
            if char2 not in dict2:
                dict2[char2] = 1
            else: dict2[char2] += 1 ## O(N)
        count1 = list(dict1.values())
        count2 = list(dict2.values())
        count1.sort()
        count2.sort()
        if count1 == count2: return True
        else: return False