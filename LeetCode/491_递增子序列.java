import java.util.*;

/*
    491. 递增子序列
    https://leetcode-cn.com/problems/increasing-subsequences/

    给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

    执行用时：5 ms, 在所有 Java 提交中击败了87.11%的用户
    内存消耗：46.9 MB, 在所有 Java 提交中击败了47.51%的用户
 */


class Solution {
    List<List<Integer>> subset = new ArrayList<>();

    public List<List<Integer>> findSubsequences(int[] nums) {
        dfs(new ArrayList<>(), Integer.MIN_VALUE, 0, nums);
        return subset;
    }

    public void dfs(List<Integer> cur, int pre, int idx, int[] nums) {
        if (idx == nums.length) {
            if (cur.size() >= 2) subset.add(cur);
        } else {
            List<Integer> temp = new ArrayList<>(cur);
            if (nums[idx] != pre) dfs(temp, pre, idx + 1, nums);
            List<Integer> temp2 = new ArrayList<>(cur);
            if (nums[idx] >= pre) {
                temp2.add(nums[idx]);
                dfs(temp2, nums[idx], idx+ 1, nums);
            }
        }
    }
}


class Solution2 {
    List<Integer> temp = new ArrayList<Integer>();
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    Set<Integer> set = new HashSet<Integer>();
    int n;

    public List<List<Integer>> findSubsequences(int[] nums) {
        n = nums.length;
        for (int i = 0; i < (1 << n); ++i) {
            findSubsequences(i, nums);
            int hashValue = getHash(263, (int) 1E9 + 7);
            if (check() && !set.contains(hashValue)) {
                ans.add(new ArrayList<Integer>(temp));
                set.add(hashValue);
            }
        }
        return ans;
    }

    public void findSubsequences(int mask, int[] nums) {
        temp.clear();
        for (int i = 0; i < n; ++i) {
            if ((mask & 1) != 0) {
                temp.add(nums[i]);
            }
            mask >>= 1;
        }
    }

    public int getHash(int base, int mod) {
        int hashValue = 0;
        for (int x : temp) {
            hashValue = hashValue * base % mod + (x + 101);
            hashValue %= mod;
        }
        return hashValue;
    }

    public boolean check() {
        for (int i = 1; i < temp.size(); ++i) {
            if (temp.get(i) < temp.get(i - 1)) {
                return false;
            }
        }
        return temp.size() >= 2;
    }
}


class Solution3 {
    List<Integer> temp = new ArrayList<Integer>();
    List<List<Integer>> ans = new ArrayList<List<Integer>>();

    public List<List<Integer>> findSubsequences(int[] nums) {
        dfs(0, Integer.MIN_VALUE, nums);
        return ans;
    }

    public void dfs(int cur, int last, int[] nums) {
        if (cur == nums.length) {
            if (temp.size() >= 2) {
                ans.add(new ArrayList<Integer>(temp));
            }
            return;
        }
        if (nums[cur] >= last) {
            temp.add(nums[cur]);
            dfs(cur + 1, nums[cur], nums);
            temp.remove(temp.size() - 1);
        }
        if (nums[cur] != last) {
            dfs(cur + 1, last, nums);
        }
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/increasing-subsequences/solution/di-zeng-zi-xu-lie-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。