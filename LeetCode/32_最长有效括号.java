import java.util.*;

/*
    32. 最长有效括号
    https://leetcode-cn.com/problems/longest-valid-parentheses/

    给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

    执行用时：3 ms, 在所有 Java 提交中击败了52.88%的用户
    内存消耗：39.6 MB, 在所有 Java 提交中击败了9.52%的用户
 */


class Solution {
    public int longestValidParentheses(String s) {
        int left = 0, right = 0;
        int res = 0;

        for (char c: s.toCharArray()) {
            if (c == '(') {
                ++left;
            } else if (c == ')') {
                ++right;
            }

            if (left == right) {
                res = Math.max(res, left * 2);
            } else if (right > left) {
                left = 0;
                right = 0;
            }
        }

        left = 0;
        right = 0;
        for (char c: new StringBuffer(s).reverse().toString().toCharArray()) {
            if (c == '(') {
                ++left;
            } else if (c == ')') {
                ++right;
            }

            if (left == right) {
                res = Math.max(res, left * 2);
            } else if (right < left) {
                left = 0;
                right = 0;
            }
        }

        return res;
    }


    public int longestValidParentheses_2(String s) {
        int maxans = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        // 始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.empty()) {
                    stack.push(i);
                } else {
                    maxans = Math.max(maxans, i - stack.peek());
                }
            }
        }
        return maxans;
    }
    // 作者：LeetCode-Solution
    // 链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
    // 来源：力扣（LeetCode）
    // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


    public int longestValidParentheses_3(String s) {
        int maxans = 0;
        int dp[] = new int[s.length()];
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == ')') {
                if (s.charAt(i - 1) == '(') {
                    dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
                } else if (i - dp[i - 1] > 0 && s.charAt(i - dp[i - 1] - 1) == '(') {
                    dp[i] = dp[i - 1] + ((i - dp[i - 1]) >= 2 ? dp[i - dp[i - 1] - 2] : 0) + 2;
                }
                maxans = Math.max(maxans, dp[i]);
            }
        }
        return maxans;
    }
    // 作者：LeetCode-Solution
    // 链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
    // 来源：力扣（LeetCode）
    // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
}


class LeetCode {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.longestValidParentheses(")()())"));
    }
}
