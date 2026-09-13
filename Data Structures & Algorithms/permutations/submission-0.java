class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        permutation(nums, cur, new boolean[nums.length]);
        return res;
    }

    public void permutation(int[] nums, List<Integer> cur, boolean[] used) {
        if(nums.length == cur.size()) {
            res.add(new ArrayList<>(cur));
            return;
        } 

        for(int i=0; i<nums.length; i++) {
            if(!used[i]) {
                cur.add(nums[i]);
                used[i] = true;
                permutation(nums, cur, used);
                cur.remove(cur.size() - 1);
                used[i]= false;
            }
        }
    }
}
