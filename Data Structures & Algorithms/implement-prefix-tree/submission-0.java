public class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

class PrefixTree {
    private TrieNode root;
    public PrefixTree() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode curr = root;
        for(char c: word.toCharArray()) {
            int index=c-'a';
            if(curr.children[index]==null) {
                curr.children[index] = new TrieNode();
            }
            curr = curr.children[index];
        }
        curr.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode cur=root;
        for(char c: word.toCharArray()) {
            int i=c-'a';
            if(cur.children[i] == null) return false;
            cur = cur.children[i];
        }
        return cur.isEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode cur=root;
        for(char c: prefix.toCharArray()) {
            int i=c-'a';
            if(cur.children[i] == null) return false;
            cur = cur.children[i];
        }
        return true;
    }
}
