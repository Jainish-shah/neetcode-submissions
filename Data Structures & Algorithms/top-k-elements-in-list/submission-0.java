class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // count the freq of each nums
        HashMap<Integer, Integer> temp = new HashMap<>();
        for(int n: nums) {
            temp.put(n, temp.getOrDefault(n, 0) + 1);
        }

        List<int[]> arr = new ArrayList<>();
        for(Map.Entry<Integer, Integer> entry: temp.entrySet()) {
            arr.add(new int[] {entry.getValue(), entry.getKey()});
        }
        arr.sort((a, b) -> b[0] - a[0]);

        int[] res = new int[k];
        for(int i=0;i<k; i++) {
            res[i] = arr.get(i)[1];
        }
        return res;
    }
}
