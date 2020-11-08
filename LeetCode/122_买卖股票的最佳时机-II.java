import java.util.*;

/*
    122. 买卖股票的最佳时机 II
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    执行用时：1 ms, 在所有 Java 提交中击败了99.54%的用户
    内存消耗：38.4 MB, 在所有 Java 提交中击败了83.35%的用户
 */


class Solution {
    public int maxProfit(int[] prices) {
        boolean buy = false;
        int start = 0;
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i] <= prices[i + 1]) {
                if (!buy) {
                    buy = true;
                    start = prices[i];
                }
            } else {
                if (buy) {
                    profit += prices[i] - start;
                    buy = false;
                }
            }
        }
        if (buy && prices[prices.length - 1] > start) {
            profit += prices[prices.length - 1] - start;
        }
        return profit;
    }
}


class Solution2 {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        for (int i = 1; i < n; ++i) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
            dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        }
        return dp[n - 1][0];
    }
}


class Solution3 {
    public int maxProfit(int[] prices) {
        int ans = 0;
        int n = prices.length;
        for (int i = 1; i < n; ++i) {
            ans += Math.max(0, prices[i] - prices[i - 1]);
            //  p_n - p_1 = (p_2 - p_1) + (p_3 - p_2) + ... + (p_n - p_{n-1})
        }
        return ans;
    }
}


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-ii-by-leetcode-s/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。