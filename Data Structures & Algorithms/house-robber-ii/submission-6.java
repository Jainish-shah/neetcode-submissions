class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];

        int[] firsthouse = new int[nums.length - 1];
        int[] secondhouse = new int[nums.length - 1];

        for (int i = 0; i < nums.length - 1; i++) {
            firsthouse[i] = nums[i];
            secondhouse[i] = nums[i + 1];
        }

        return Math.max(robber(firsthouse), robber(secondhouse));
    }

    public int robber(int[] house) {
        if (house.length == 0) return 0;
        if (house.length == 1) return house[0];

        int[] dp = new int[house.length];
        dp[0] = house[0];
        dp[1] = Math.max(house[0], house[1]);

        for (int i = 2; i < house.length; i++) {
            dp[i] = Math.max(house[i] + dp[i - 2], dp[i - 1]);
        }

        return dp[house.length - 1];
    }
}
