class Solution {
    public String minWindow(String s, String t) {
       if(s.length() < t.length()) return "";
       if(t.isEmpty()) return "";

       Map<Character, Integer> tCount = new HashMap<>();
       Map<Character, Integer> window = new HashMap<>();

       for(char c:t.toCharArray()) {
        tCount.put(c, tCount.getOrDefault(c, 0)+1);
       } 

       int l=0, r=0, min=Integer.MAX_VALUE, start=0, required=tCount.size(), have=0;
       for(r=0; r<s.length(); r++) {
        char c = s.charAt(r);
        window.put(c, window.getOrDefault(c, 0)+1);
        if(tCount.containsKey(c) && window.get(c).equals(tCount.get(c))) {
            have++;
        }

        while(have == required) {
            if(r-l+1 < min) {
                min = r-l+1;
                start = l;
            }

            char leftChar = s.charAt(l);
            window.put(leftChar, window.getOrDefault(leftChar, 0)-1);
            if(tCount.containsKey(leftChar) && window.get(leftChar)< tCount.get(leftChar)) {
                have--;
            }
            l++;
        }
       }
       return min == Integer.MAX_VALUE? "" : s.substring(start, start+min);
    }
}
