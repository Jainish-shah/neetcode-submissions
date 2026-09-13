class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        res = new ArrayList<>();
        Arrays.sort(nums);
        List<Integer> cur = new ArrayList<>();
        dfs(nums, cur, 0);
        return res;
    }

    public void dfs(int[] nums, List<Integer> cur, int i) {
        if(i==nums.length) {
            res.add(new ArrayList<>(cur));
            return;
        }
        cur.add(nums[i]);
        dfs(nums, cur, i+1);
        cur.remove(cur.size() - 1);
        while(i+1 < nums.length && nums[i] == nums[i+1]) {
            i++;
        }
        dfs(nums, cur, i+1);
    }
}
