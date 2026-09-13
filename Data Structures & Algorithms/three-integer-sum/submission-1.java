class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

      Arrays.sort(nums);

      for(int i=0; i<nums.length; i++) {
        if(i>0 && nums[i] == nums[i-1]) {
          continue;
        }
        List<Integer> list = new ArrayList<>();
        int j=i+1;
        int k=nums.length-1;
        while(j<k) {
          int sum = nums[i] + nums[j] + nums[k];
          if(sum == 0) {
            list.add(nums[i]);
            list.add(nums[j]);
            list.add(nums[k]);
            if(!result.contains(list)) {
              result.add(list);
              list = new ArrayList<>();
            }
            while(j<k && nums[j] == nums[j+1]) j++;
            while(j<k && nums[k] == nums[k-1]) k--;
        }
        if(sum<0) {
          j++;
        } else {
          k--;
        }
      }
    }  
    return result; 
    }
}
