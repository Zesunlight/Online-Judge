import java.util.*;

/*
    117. 填充每个节点的下一个右侧节点指针 II
    https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/

    给定一个二叉树，填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
    如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
    初始状态下，所有 next 指针都被设置为 NULL。

    执行用时：2 ms, 在所有 Java 提交中击败了45.77%的用户
    内存消耗：38.7 MB, 在所有 Java 提交中击败了25.53%的用户
 */


/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        Queue<Node> queue = new LinkedList<>();
        if (root == null) return null;
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            queue.offer(null);
            Node top = queue.poll();
            for (int i = 0; i < size; i++) {
                Node next = queue.poll();
                top.next = next;
                if (top.left != null) queue.offer(top.left);
                if (top.right != null) queue.offer(top.right);
                top = next;
            }
        }
        return root;
    }
}


class Solution2 {
    Node last = null, nextStart = null;

    public Node connect(Node root) {
        if (root == null) {
            return null;
        }
        Node start = root;
        while (start != null) {
            last = null;
            nextStart = null;
            for (Node p = start; p != null; p = p.next) {
                if (p.left != null) {
                    handle(p.left);
                }
                if (p.right != null) {
                    handle(p.right);
                }
            }
            start = nextStart;
        }
        return root;
    }

    public void handle(Node p) {
        if (last != null) {
            last.next = p;
        } 
        if (nextStart == null) {
            nextStart = p;
        }
        last = p;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-15/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    public void dfs(Node left, Node right) {
        if (left == null || right == null) return;
        left.next = right;
        dfs(left.left, left.right);
        dfs(right.left, right.right);
        dfs(left.right, right.left);
    }
    
    public Node connect(Node root) {
        if (root == null) return null;
        dfs(root.left, root.right);
        return root;
    }
}

// https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-j-3/290307