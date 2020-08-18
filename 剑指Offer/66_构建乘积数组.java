/*
=================================================
Problem: 面试题 66. 构建乘积数组
Website: https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
Difficulty: 简单
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 3 ms, 在所有 Python3 提交中击败了12.03%的用户
Memory Usage: 52.7 MB, 在所有 Python3 提交中击败了17.00%的用户
==================================================*/


class Solution {
    public int[] constructArr(int[] a) {
        int n = a.length;
        if (n <= 1) return a;
        
        int[] front = new int[n], back = new int[n], res = new int[n];
        front[0] = a[0];
        back[n - 1] = a[n - 1];
        for (int i = 1; i < n; i++) {
            front[i] = front[i - 1] * a[i];
            back[n - i - 1] = back[n - i] * a[n - i - 1];
        }

        res[0] = back[1];
        res[n - 1] = front[n - 2];
        for (int i = 1; i < n - 1; i++) {
            res[i] = front[i - 1] * back[i + 1];
        }
        return res;
    }
}


class Solution2 {
    public int[] constructArr(int[] a) {
        if(a.length == 0) return new int[0];
        int[] b = new int[a.length];
        b[0] = 1;
        int tmp = 1;
        for(int i = 1; i < a.length; i++) {
            b[i] = b[i - 1] * a[i - 1];
        }
        for(int i = a.length - 2; i >= 0; i--) {
            tmp *= a[i + 1];
            b[i] *= tmp;
        }
        return b;
    }
}

// 作者：jyd
// 链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/mian-shi-ti-66-gou-jian-cheng-ji-shu-zu-biao-ge-fe/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。