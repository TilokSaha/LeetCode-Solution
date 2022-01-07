class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)   # <-------- converting string to dict of character and count of character pair
        for i,item in enumerate(s):
            if count[item] ==1: # <------ first occuring character with the count of 1
                return i
        return -1