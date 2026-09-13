class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        StringBuilder stack = new StringBuilder();
        backtracking(0, 0, n, result, stack);
        return result;
    }

    public void backtracking(int Open, int Close, int n, List<String> result, StringBuilder stack) {
        if(Open == n && Open == Close) {
            result.add(stack.toString());
            return;
        }

        if(Open < n) {
            stack.append('(');
            backtracking(Open + 1, Close, n, result, stack);
            stack.deleteCharAt(stack.length()-1);
        }
        if(Open>Close) {
            stack.append(')');
            backtracking(Open, Close+1, n, result, stack);
            stack.deleteCharAt(stack.length()-1);
        }
    }
}