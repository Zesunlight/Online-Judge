import java.util.*;

/*
    77. 组合
    https://leetcode-cn.com/problems/combinations/

    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

    执行用时：107 ms, 在所有 Java 提交中击败了5.26%的用户
    内存消耗：39.9 MB, 在所有 Java 提交中击败了86.99%的用户
 */


class Solution {
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        combine(1, n, k, new ArrayList<>());
        return res;
    }

    public void combine(int s, int n, int k, List<Integer> example) {
        if (k == 0) res.add(new ArrayList<>(example));
        else {
            for (int i = s; i <= n; i++) {
                example.add(i);
                combine(i + 1, n, k - 1, example);
                example.remove((Integer) i);
            }
        }
    }
}


class Solution {
    List<Integer> temp = new ArrayList<Integer>();
    List<List<Integer>> ans = new ArrayList<List<Integer>>();

    public List<List<Integer>> combine(int n, int k) {
        dfs(1, n, k);
        return ans;
    }

    public void dfs(int cur, int n, int k) {
        // 剪枝：temp 长度加上区间 [cur, n] 的长度小于 k，不可能构造出长度为 k 的 temp
        if (temp.size() + (n - cur + 1) < k) {
            return;
        }
        // 记录合法的答案
        if (temp.size() == k) {
            ans.add(new ArrayList<Integer>(temp));
            return;
        }
        // 考虑选择当前位置
        temp.add(cur);
        dfs(cur + 1, n, k);
        temp.remove(temp.size() - 1);
        // 考虑不选择当前位置
        dfs(cur + 1, n, k);
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/combinations/solution/zu-he-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。