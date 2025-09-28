class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ## must use only constant extra space - no dictionary/array which depends on N
        ## store in the input character array
        ## given it asks for consecutive repeating characters of EACH GROUP, we only need to consider each letter once
        ## start with index i, we scans through the entire array
        ## append at the end
        i = 0
        count = 0
        current = chars[0]
        n = len(chars)
        while i < n:
            char = chars[0]
            if current == char:
                count += 1
                if i == n-1:
                    chars.append(char)
                    if count > 1:
                        chars.extend(list(str(count)))
            else:
                chars.append(current)
                if count > 1:
                    chars.extend(list(str(count)))
                count = 1
                current = char
                if i == n-1:
                    chars.append(current)

            chars.pop(0)
            i += 1
        return len(chars)