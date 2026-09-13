class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> r = new HashMap<>();

        for(String s: strs) {
            char[] c = s.toCharArray();
            Arrays.sort(c);
            String sorted = new String(c);
            r.putIfAbsent(sorted, new ArrayList<>());
            r.get(sorted).add(s);
        }
        return new ArrayList<>(r.values());
    }
}
