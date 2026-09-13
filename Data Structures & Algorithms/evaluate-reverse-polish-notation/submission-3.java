class Solution {
    public int evalRPN(String[] tokens) {
        HashSet<String> set = new HashSet<>();
        set.add("+");
        set.add("-");
        set.add("/");
        set.add("*");

        int a = 0, b=0;
        Stack<Integer> stack = new Stack<>();
        for(String s: tokens) {
            if(set.contains(s) && !stack.isEmpty()) {
                a = stack.pop();
                b = stack.pop();
                if(s.equals("+")) stack.push(a+b);
                if(s.equals("-")) stack.push(b-a);
                if(s.equals("*")) stack.push(a*b);
                if(s.equals("/")) stack.push(b/a);
            } else {
                stack.push(Integer.parseInt(s));
            }
        }
        return stack.pop();
    }
}