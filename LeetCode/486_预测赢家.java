import java.util.*;

/*
    486. 预测赢家
    https://leetcode-cn.com/problems/predict-the-winner/

    给定一个表示分数的非负整数数组。 
    玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。
    每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。
    最终获得分数总和最多的玩家获胜。
    给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

    执行用时：0 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：37.1 MB, 在所有 Java 提交中击败了47.11%的用户
 */


class Solution {
    int[] n;
    int[] preSum;
    int[][] dp;

    public boolean PredictTheWinner(int[] nums) {
        n = nums;
        preSum = new int[n.length];
        preSum[0] = n[0];
        dp = new int[n.length][n.length];
        
        for (int i = 1; i < preSum.length; i++) {
            preSum[i] = preSum[i - 1] + n[i];
        }
        int former = PredictTheWinner(0, n.length - 1);
        return former >= preSum[n.length - 1] - former;
    }

    public int PredictTheWinner(int left, int right) {
        if (dp[left][right] != 0) return dp[left][right];
        
        if (left == right) return n[left];

        int next = Math.min(PredictTheWinner(left + 1, right), PredictTheWinner(left, right - 1));
        if (left == 0) {
            return dp[left][right] = preSum[right] - next;
        } else {
            return dp[left][right] = preSum[right] - preSum[left - 1] - next;
        }
    }
}

// https://leetcode-cn.com/problems/predict-the-winner/solution/ling-he-bo-yi-ji-yi-hua-0ms-gao-ding-by-time-limit/


class Solution {
    // 先手分数为正，后手为负

    public boolean PredictTheWinner(int[] nums) {
        return total(nums, 0, nums.length - 1, 1) >= 0;
    }

    public int total(int[] nums, int start, int end, int turn) {
        if (start == end) {
            return nums[start] * turn;
        }
        int scoreStart = nums[start] * turn + total(nums, start + 1, end, -turn);
        int scoreEnd = nums[end] * turn + total(nums, start, end - 1, -turn);
        return Math.max(scoreStart * turn, scoreEnd * turn) * turn;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/predict-the-winner/solution/yu-ce-ying-jia-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。