class Solution {
    public int jump(int[] nums) {
        if(nums == null || nums.length < 1) {
            return 0;
        }

        int jump = 0, far = 0, end = 0;
        for(int i=0; i<nums.length-1; i++) {
            far = Math.max(far, nums[i] + i);
            if(end == i) {
                end = far;
                jump++;
                if(nums[i] == 0) {
                    continue;
                }
            }
        }
        return jump;
    }
}
