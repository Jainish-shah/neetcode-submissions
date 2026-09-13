class KthLargest {
    private PriorityQueue<Integer> pq;
    int K;
    public KthLargest(int k, int[] nums) {
        K = k;
        this.pq = new PriorityQueue<>();
        for(int n:nums) {
            pq.add(n);
            if(pq.size() > K) {
                pq.poll();
            } 
        }
    }
    
    public int add(int val) {
        pq.add(val);
        if(pq.size() > K) {
            pq.poll();
        }
        return pq.peek();
    }
}
