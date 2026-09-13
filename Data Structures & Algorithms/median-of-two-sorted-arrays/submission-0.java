class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] arr = new int[m+n];
        for(int i=0; i<m; i++) {
            arr[i] = nums1[i];
        }
        for(int j=0; j<n; j++) {
            arr[m+j] = nums2[j];
        }
        Arrays.sort(arr);

        int len = arr.length;
        if(len%2 == 0) {
            return (arr[len/2-1] + arr[len/2])/2.0;
        } else {
            return arr[len/2];
        }
    }
}
