import java.util.*;

/*
    410. 分割数组的最大值
    https://leetcode-cn.com/problems/split-array-largest-sum/

    给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。
    设计一个算法使得这 m 个子数组各自和的最大值最小。

    执行用时：0 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：37.2 MB, 在所有 Java 提交中击败了33.33%的用户
 */


class Solution {
    public int splitArray(int[] nums, int m) {
        if (nums.length == 0) return 0;
        long left = nums[0], right = nums[0];
        for (int n : nums) {
            left = Math.max(left, n);
            right += n;
        }

        while (left < right) {
            long mid = left + (right - left) / 2;
            if (satisfy(mid, m, nums)) right = mid;
            else left = mid + 1;
        }

        return (int)left;
    }

    public boolean satisfy(long s, int m, int[] nums) {
        long partSum = 0;
        for (int value : nums) {
            partSum += value;
            if (partSum > s) {
                m--;
                partSum = value;
            }
            if (m == 0) return false;
        }
        return true;
    }
}


class Solution2 {
    public int splitArray(int[] nums, int m) {
        int n = nums.length;
        int[][] f = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(f[i], Integer.MAX_VALUE);
        }
        int[] sub = new int[n + 1];
        for (int i = 0; i < n; i++) {
            sub[i + 1] = sub[i] + nums[i];
        }
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= Math.min(i, m); j++) {
                for (int k = 0; k < i; k++) {
                    f[i][j] = Math.min(f[i][j], Math.max(f[k][j - 1], sub[i] - sub[k]));
                }
            }
        }
        return f[n][m];
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/split-array-largest-sum/solution/fen-ge-shu-zu-de-zui-da-zhi-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
