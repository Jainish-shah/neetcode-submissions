class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        for c in s:
            s1[c] = 1+s1.get(c, 0)
        s2 = {}
        for c in t:
            s2[c] = 1+ s2.get(c, 0)
        return True if s1 == s2 else False 
