import random
class RandomizedSet(object):

    def __init__(self):
        self.vals = [] ## one to store values for selection
        self.idx = {} ##one to store index
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        n = len(self.vals)
        if val not in self.idx:
            self.idx[val] = n
            self.vals.append(val)
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.vals:
            return False
        elif val == self.vals[-1]:
            del self.idx[val]
            self.vals.pop()
        else:
            temp = self.vals[-1]
            self.vals[self.idx[val]] = temp
            self.vals.pop()
            self.idx[temp] = self.idx[val]
            del self.idx[val]
        return True
    def getRandom(self):
        """
        :rtype: int
        """
        res = random.choice(self.vals)
        return res