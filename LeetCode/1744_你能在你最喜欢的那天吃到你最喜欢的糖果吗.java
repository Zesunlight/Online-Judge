import java.util.*;

/*
    1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
    https://leetcode-cn.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day

    给你一个下标从 0 开始的正整数数组candiesCount，其中candiesCount[i]表示你拥有的第i类糖果的数目。
    同时给你一个二维数组queries，其中queries[i] = [favoriteTypei, favoriteDayi, dailyCapi]。

    你按照如下规则进行一场游戏：
    你从第0天开始吃糖果。
    你在吃完 所有第 i - 1类糖果之前，不能吃任何一颗第 i类糖果。
    在吃完所有糖果之前，你必须每天 至少吃 一颗糖果。
    请你构建一个布尔型数组answer，满足answer.length == queries.length 。
    answer[i]为true的条件是：在每天吃不超过dailyCapi颗糖果的前提下，你可以在第favoriteDayi天吃到第favoriteTypei类糖果；
    否则 answer[i]为 false。注意，只要满足上面 3 条规则中的第二条规则，你就可以在同一天吃不同类型的糖果。

    请你返回得到的数组answer。

    执行用时：9 ms
    内存消耗：75.1 MB
 */


class Solution {
    public boolean[] canEat(int[] candiesCount, int[][] queries) {
        boolean[] ans = new boolean[queries.length];
        long[] accumulate = new long[candiesCount.length + 1];
        accumulate[0] = 0;
        for (int i = 0; i < candiesCount.length; i++) {
            accumulate[i + 1] = accumulate[i] + candiesCount[i];
        }

        for (int i = 0; i < queries.length; i++) {
            long lower = queries[i][1] + 1;
            long high = lower * queries[i][2];  // 注意int溢出的问题
            int type = queries[i][0] + 1;

            ans[i] = (lower <= accumulate[type]) && (high > accumulate[type - 1]);
//            if ((lower > accumulate[type]) || (high <= accumulate[type - 1])) {
//                ans[i] = false;
//            } else {
//                ans[i] = true;
//            }
        }

        return ans;
    }
}
