class Solution {
    public boolean canJump(int[] nums) {
        if(nums == null || nums.length == 0) {
            return false;
        } 
        int end = 0, far =0;
        for(int i=0; i<nums.length-1; i++) {
            far = Math.max(far, nums[i] + i);

            if(nums[i] == 0)
                if(far == i) 
                    return false;
            if(end == i) {
                end = far;

                // if(nums[i] == 0)
                //     if(far == i) 
                //         return false;
            }
        }
        return true;
    }
}
