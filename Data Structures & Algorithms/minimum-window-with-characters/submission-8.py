class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case 
        if t == "":
            return ""
        
        # freq count for T
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # initialize the empty array and resLen
        res = [-1, -1]
        resLen = float('inf')
        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break
                    
                if flag and (j- i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]
        
        l , r = res
        return s[l: r + 1] if resLen != float('inf') else ""