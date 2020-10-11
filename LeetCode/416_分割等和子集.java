import java.util.*;

/*
    416. 分割等和子集
    https://leetcode-cn.com/problems/partition-equal-subset-sum/

    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

    执行用时：55 ms, 在所有 Java 提交中击败了17.65%的用户
    内存消耗：40.3 MB, 在所有 Java 提交中击败了5.16%的用户
 */


class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 2 == 1) return false;
        boolean[][] dp = new boolean[nums.length][sum + 1];
        for (int i = 0; i < nums.length; i++) {
            dp[i][0] = true;
        }

        int preSum = 0;
        for (int i = 0; i < nums.length; i++) {
            preSum += nums[i];
            if (i < 1) {
                dp[i][nums[i]] = true;
                continue;
            }
            for (int j = 1; j < preSum + 1; j++) {
                if (nums[i] <= j) {
                    dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]];
                } else dp[i][j] = dp[i-1][j];
            }
        }

        return dp[nums.length - 1][sum / 2];
    }
}


class Solution {
    public boolean canPartition(int[] nums) {
        int n = nums.length;
        if (n < 2) {
            return false;
        }
        int sum = 0, maxNum = 0;
        for (int num : nums) {
            sum += num;
            maxNum = Math.max(maxNum, num);
        }
        if (sum % 2 != 0) {
            return false;
        }
        int target = sum / 2;
        if (maxNum > target) {
            return false;
        }
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            for (int j = target; j >= num; --j) {
                dp[j] |= dp[j - num];
            }
        }
        return dp[target];
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。