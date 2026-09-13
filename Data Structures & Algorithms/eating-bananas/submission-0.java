class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l=1, r=getmaxpile(piles);
        while(l<r) {
            int k=l + (r-l)/2;
            if(canFinish(piles, k, h)) {
                r=k;
            } else {
                l=k+1;
            }
        }
        return l;
    }

    public boolean canFinish(int[] piles, int k, int h) {
        int hours = 0;
        for(int i:piles) {
            hours += Math.ceil((double) i/k);
        }
        return (hours <= h);
    }

    public int getmaxpile(int[] piles) {
        int max = Integer.MIN_VALUE;
        for(int i:piles) {
            max = Math.max(max, i);
        }
        return max;
    }
}
