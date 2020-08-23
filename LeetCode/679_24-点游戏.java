import java.util.*;

/*
    679. 24 点游戏
    https://leetcode-cn.com/problems/24-game/

    你有 4 张写有 1 到 9 数字的牌。
    你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

    执行用时：2 ms, 在所有 Java 提交中击败了89.26%的用户
    内存消耗：39.5 MB, 在所有 Java 提交中击败了78.72%的用户
 */


cclass Solution {
    public boolean judgePoint24(int[] nums) {
        double[] d = new double[nums.length];
        for (int i = 0; i < nums.length; i++) {
            d[i] = (double) nums[i];
        }

        return judgePoint24(d);
    }

    public boolean judgePoint24(double[] nums) {
        if (nums.length == 1) {
            return Math.abs(nums[0] - 24) < 1e-6;
        }

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i == j) continue;
                double[] shrink = new double[nums.length - 1];
                int idx = 0;
                for (int k = 0; k < nums.length; k++) {
                    if (k != i && k != j) {
                        shrink[idx] = nums[k];
                        idx++;
                    }
                }
                shrink[idx] = nums[i] + nums[j];
                if (judgePoint24(shrink)) return true;
                shrink[idx] = nums[i] - nums[j];
                if (judgePoint24(shrink)) return true;
                shrink[idx] = nums[i] * nums[j];
                if (judgePoint24(shrink)) return true;
                if (nums[j] != 0) {
                    shrink[idx] = nums[i] / nums[j];
                    if (judgePoint24(shrink)) return true;
                }
            }
        }
        return false;
    }
}


/*
一共有 4 个数和 3 个运算操作，因此可能性非常有限。一共有多少种可能性呢？

首先从 4 个数字中有序地选出 2 个数字，共有 4×3=12 种选法，
并选择加、减、乘、除 4 种运算操作之一，用得到的结果取代选出的 2 个数字，剩下 3 个数字。

然后在剩下的 3 个数字中有序地选出 2 个数字，共有 3×2=6 种选法，
并选择 4 种运算操作之一，用得到的结果取代选出的 2 个数字，剩下 22 个数字。

最后剩下 2 个数字，有 2 种不同的顺序，并选择 4 种运算操作之一。

因此，一共有 12×4×6×4×2×4=9216 种不同的可能性。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/24-game/solution/24-dian-you-xi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/