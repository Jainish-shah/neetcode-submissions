class Solution {
    public int maxProfit(int[] prices) {
        int l=0, r=0, profit=0;
        int n=prices.length;
        while(r<n) {
            if(prices[r] > prices[l]) {
                profit = Math.max(profit, prices[r] - prices[l]);
            } else {
                l=r;
            }
            r++;
        }
        return profit;
    }
}
