class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;

        char sTemp[] = s.toCharArray();
        Arrays.sort(sTemp);

        char tTemp[] = t.toCharArray();
        Arrays.sort(tTemp);

        return Arrays.equals(sTemp, tTemp);
    }
}
