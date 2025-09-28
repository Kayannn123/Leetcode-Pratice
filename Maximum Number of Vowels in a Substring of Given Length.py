class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        window = list(s[:k])
        current = 0

        for char in window:
            if char in vowels:
                current += 1
        
        result = current
        for i in range(k, len(s)):
            initial = window.pop(0)
            char = s[i]
            window.append(char)
            if initial in vowels:
                current -= 1
            if char in vowels:
                current += 1
            if current > result:
                result = current
        return result
        