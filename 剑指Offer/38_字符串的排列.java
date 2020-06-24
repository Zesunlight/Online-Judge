import java.util.*;

/*
    38. 字符串的排列
    https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/

    输入一个字符串，打印出该字符串中字符的所有排列。
    你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

    执行用时：9 ms, 在所有 Java 提交中击败了97.17%的用户
    内存消耗：44.2 MB, 在所有 Java 提交中击败了100.00%的用户
 */

class Solution {
    ArrayList<String> res = new ArrayList<>();
    char[] c;

    public String[] permutation(String s) {
        c = s.toCharArray();
        dfs(0);
        return res.toArray(new String[0]);
    }

    public void dfs(int start) {
        if (start == c.length - 1) {
            res.add(String.valueOf(c));
            return;
        }

        HashSet<Character> set = new HashSet<>();
        for (int i = start; i < c.length; i++) {
            if (set.contains(c[i])) {
                continue;
            } else {
                set.add(c[i]);
            }
            swap(i, start);
            dfs(start + 1);
            swap(i, start);
        }
    }

    public void swap(int a, int b) {
        char tmp = c[a];
        c[a] = c[b];
        c[b] = tmp;
    }
}


class LeetCode {
    public static void main(String[] args) {
        Solution s = new Solution();
        for (String str : s.permutation("abc")) {
            System.out.println(str);
        }
    }
}