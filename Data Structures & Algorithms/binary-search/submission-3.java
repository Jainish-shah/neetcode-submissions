class Solution {
    public int binary_search(int l, int u, int[] nums, int target) {
        if(l>u) return -1;
        int m = l + (u-l) /2;
        if(nums[m] == target) return m;
        return (nums[m] < target) ? binary_search(m+1, u, nums, target) : binary_search(l, m-1, nums, target);
    }

    public int search(int[] nums, int target) {
        return binary_search(0, nums.length-1, nums, target);
    }
    
}
