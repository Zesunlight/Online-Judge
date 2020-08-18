/*
=================================================
Problem: 面试题 62. 圆圈中最后剩下的数字
Website: https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
Difficulty: 简单
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 12 ms, 在所有 Python3 提交中击败了39.68%的用户
Memory Usage: 41.8 MB, 在所有 Python3 提交中击败了16.82%的用户
==================================================*/


class Solution {
    public int lastRemaining(int n, int m) {
        if (n == 1) return 0;
        int delete = (m - 1) % n;
        int result = lastRemaining(n - 1, m);
        return (result + delete + 1) % n;
    }
}


/*
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-by-lee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
