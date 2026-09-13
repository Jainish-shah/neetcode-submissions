class Solution {
    public int maxArea(int[] heights) {
        int max = Integer.MIN_VALUE;
        int j=heights.length-1;
        int w=0, h=0;
        int i=0;
        while(i<j) {
                w=j-i;
                h=Math.min(heights[i], heights[j]);
                int area = w*h;
                if(max<area) {
                    max = area;
                }
                if(heights[i] < heights[j]) i++;
                else j--;
            }
        return max;
    }
}
