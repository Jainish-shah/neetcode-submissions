class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total_cost = 0, total_gas = 0;
        for(int i=0; i<cost.length; i++) {
            total_cost += cost[i];
            total_gas += gas[i];
        }

        if(total_cost > total_gas) 
            return -1; // trip not possible

        int startIndex = 0, curGas = 0;
        for(int i=0; i<cost.length; i++) {
            curGas += gas[i] - cost[i];
            if(curGas < 0)  {
                curGas = 0;
                startIndex = i+1;
            }
        }   
        return startIndex;
    }
}
