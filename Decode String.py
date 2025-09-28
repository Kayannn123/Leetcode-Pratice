class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        ## start to pop to get a temp list
        ## when reach [, look for digit (another temp)
        ## when reach another character or the stack is empty, append the digit*temp by the end of stack
        stack, temp, digit = [], [], []
        for char in s:
            if char == "]":
                while True: ## first get strings
                    current = stack.pop()
                    if current == "[": break
                    temp.append(current)
                while stack != [] and stack[-1].isnumeric(): 
                    digit.append(stack.pop())
                temp2 = []
                while temp:
                    temp2.append(temp.pop())
                digit2 = []
                while digit:
                    digit2.append(digit.pop())
                num = int("".join(digit2))
                stack.extend(num*temp2)
                digit, temp = [], [] ## reinitialize
            else:
                stack.append(char)
        result = "".join(stack)
        return result