class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) {
            return false;
        }

        HashMap<Character, Integer> scount = new HashMap<>();
        HashMap<Character, Integer> tcount = new HashMap<>();

        for(char c: s.toCharArray()) { // Enhanced for loop
            scount.put(c, scount.getOrDefault(c,0)+1);
        }
        for(char c: t.toCharArray()) { // Enhanced for loop
            tcount.put(c, tcount.getOrDefault(c,0)+1);
        }
        return scount.equals(tcount);
    }
}
