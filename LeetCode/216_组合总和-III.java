import java.util.*;

/*
    216. 组合总和 III
    https://leetcode-cn.com/problems/combination-sum-iii/

    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

    执行用时：1 ms, 在所有 Java 提交中击败了69.81%的用户
    内存消耗：37 MB, 在所有 Java 提交中击败了77.27%的用户
 */


class Solution {
    int[] visit = new int[10];
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combinationSum3(int k, int n) {
        combinationSum3(k, n, new ArrayList<>());
        return res;
    }

    public void combinationSum3(int k, int n, List<Integer> temp) {
        int start = 1;
        if (temp.size() > 0) {
            start = temp.get(temp.size() - 1) + 1;
        }

        if (k == 1 && n >= start && n <= 9 && visit[n] == 0) {
            temp.add(n);
            res.add(new ArrayList<>(temp));
            temp.remove(temp.size() - 1);
        } else {
            for (int i = start; i < 10; i++) {
                if (visit[i] == 0) {
                    temp.add(i);
                    visit[i] = 1;
                    combinationSum3(k - 1, n - i, temp);
                    visit[i] = 0;
                    temp.remove(temp.size() - 1);
                }
            }
        }
    }
}


class Solution2 {
    // 二进制（子集）枚举
    List<Integer> temp = new ArrayList<Integer>();
    List<List<Integer>> ans = new ArrayList<List<Integer>>();

    public List<List<Integer>> combinationSum3(int k, int n) {
        for (int mask = 0; mask < (1 << 9); ++mask) {
            if (check(mask, k, n)) {
                ans.add(new ArrayList<Integer>(temp));
            }
        }
        return ans;
    }

    public boolean check(int mask, int k, int n) {
        temp.clear();
        for (int i = 0; i < 9; ++i) {
            if (((1 << i) & mask) != 0) {
                temp.add(i + 1);
            }
        }
        if (temp.size() != k) {
            return false;
        }
        int sum = 0;
        for (int num : temp) {
            sum += num;
        }
        return sum == n;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/combination-sum-iii/solution/zu-he-zong-he-iii-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。