class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for(int r=0; r<matrix.length;r++) {
            for(int c=0; c<matrix[r].length; c++) {
                if(target == matrix[r][c]) {
                    return true;
                }
            }
        }
        return false;
    }
}
