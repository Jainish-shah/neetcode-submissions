class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;
        while(l<r) {
            int current = numbers[l] + numbers[r];
            if(current == target) {
                return new int[]{l+1, r+1};
            }
            else if(current < target) 
                l++;
            else 
                r--;
        }
        return new int[0];
    }
}
