from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        R=Counter(ransomNote)  # <------ string to dict 'char' : 'number of element in the string'
        M=Counter(magazine)
        for i in R:
            if not (i in M and R[i]<=M[i]): # <--------- same as anagram but the number count should be less than or equals to
                return False
        return True