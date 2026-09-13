class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        List<String> part = new ArrayList<>();

        dfs(0,s,res,part);
        return res;
    }

    private void dfs(int i, String s, List<List<String>> res, List<String> part) {
        if(i >= s.length()) {
            res.add(new ArrayList<>(part));
        }
        for(int j=i; j<s.length(); j++) {
            if(isPal(s, i, j)) {
                part.add(s.substring(i, j+1));
                dfs(j+1, s, res, part);
                part.remove(part.size() - 1);
            }
        }
    }

    private boolean isPal(String s, int l, int r) {
        while(l<r) {
            if(s.charAt(l) != s.charAt(r)) {
                return false;
            }
            r--;
            l++;
        }
        return true;
    }
}
