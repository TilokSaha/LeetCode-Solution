from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S=Counter(s)   # <-------- counting each character in a string and stores them in key value pair like 'char' : 'number'
        T=Counter(t)
        for i in S:
            if not (i in T and S[i]==T[i] and len(S)==len(T)):    # <----- checking if they have same amount of characters and count of characters
                return False
        return True