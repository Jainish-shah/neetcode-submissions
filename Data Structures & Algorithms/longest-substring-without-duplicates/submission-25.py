class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 0
        maxlen = 0
        
        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen.get(s[r]) + 1, l)
            seen[s[r]] = r
            maxlen = max(maxlen, r - l + 1)
        return maxlen