import java.util.*;

/*
    309. 最佳买卖股票时机含冷冻期
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

    执行用时：35 ms, 在所有 Java 提交中击败了19.55%的用户
    内存消耗：37.6 MB, 在所有 Java 提交中击败了33.33%的用户
 */


class Solution {
    public int maxProfit(int[] prices) {
        int[] stop = new int[prices.length];
        int res = 0;
        for (int i = 1; i < prices.length; ++i) {
            stop[i] = stop[i - 1];
            for (int j = i - 1; j >= 0; --j) {
                if (prices[j] < prices[i]) {
                    int history = (j > 2 ? stop[j - 2]: 0) + prices[i] - prices[j];
                    stop[i] = Math.max(stop[i], history);
                }
            }
            res = Math.max(res, stop[i]);
        }
        return res;
    }
}


class Solution_2 {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }

        int n = prices.length;
        // f[i][0]: 手上持有股票的最大收益
        // f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        // f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        int[][] f = new int[n][3];
        f[0][0] = -prices[0];
        for (int i = 1; i < n; ++i) {
            f[i][0] = Math.max(f[i - 1][0], f[i - 1][2] - prices[i]);
            f[i][1] = f[i - 1][0] + prices[i];
            f[i][2] = Math.max(f[i - 1][1], f[i - 1][2]);
        }
        return Math.max(f[n - 1][1], f[n - 1][2]);
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-qi-4/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
