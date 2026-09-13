class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0, r = 0, n = s.length();
        int maxLength = 0, len=0;
        char[] c = s.toCharArray();
        HashSet<Character> str = new HashSet<>();
        while(r<n) {
            if(str.contains(c[r])) {
                str.remove(c[l]);
                l++;
            } else {
                len = r-l+1;
                maxLength = Math.max(maxLength, len);
                str.add(c[r]);
                r++;
            }
        }

        return maxLength;
    }
}
