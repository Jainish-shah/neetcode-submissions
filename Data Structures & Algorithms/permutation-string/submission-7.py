class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        count1 = {}
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
        
        need = len(count1)
        count2, matches = {}, 0
        l = 0
        for r in range(len(s2)):
            lc = s2[r]
            count2[lc] = 1 + count2.get(lc, 0)
            # expand the window
            if count2[lc] == count1.get(lc, 0):
                matches += 1
            elif count2[lc] == 1 + count1.get(lc, 0):
                matches -= 1
            
            # strink the window from the left pointer
            if r - l + 1 > len(s1):
                lc = s2[l]
                count2[lc] -= 1
                
                if count2[lc] == count1.get(lc, 0):
                    matches += 1
                elif count2[lc] == count1.get(lc, 0) - 1:
                    matches -= 1
                l += 1
            if need == matches:
                return True
        return False
