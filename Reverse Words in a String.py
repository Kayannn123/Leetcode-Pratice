class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s = s.strip()
        ls = list(s)
        counter = []
        for i in range(len(ls)):
            character = ls[i]
            if character != " ":
                counter.append(character)
            else:
                if counter != []:
                    stack.append("".join(counter))
                counter = []
        stack.append("".join(counter))
        result = []
        while stack != []:
            result.append(stack.pop())
        return " ".join(result)