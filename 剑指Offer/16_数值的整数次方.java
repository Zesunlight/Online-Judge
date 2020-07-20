import java.util.*;

/*
    16. 数值的整数次方
    https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/

    实现函数double Power(double base, int exponent)，
    求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

    执行用时：1 ms, 在所有 Java 提交中击败了94.37%的用户
    内存消耗：37.2 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class Solution {

    public double myPow(double x, long n) {
        int sign = 1;
        if (n < 0) {
            n = -n;
            sign = -1;
        }

        double res = 1, temp = x;
        while (n > 0) {
            if ((n & 1) == 1) {
                res *= temp;
            }
            temp *= temp;
            n >>= 1;
        }

        if (sign == -1) res = 1 / res;
        return res;
    }

}


class Solution2 {
    public double myPow(double x, int n) {
        // Java 代码中 int32 变量 n∈[−2147483648,2147483647] ，
        // 因此当 n=−2147483648 时执行 n=−n 会因越界而赋值出错。
        // 解决方法是先将 n 存入 long 变量 b ，后面用 b 操作即可。

        if(x == 0) return 0;
        long b = n;
        double res = 1.0;
        if(b < 0) {
            x = 1 / x;
            b = -b;
        }
        while(b > 0) {
            if((b & 1) == 1) res *= x;
            x *= x;
            b >>= 1;
        }
        return res;
    }
}

// 作者：jyd
// 链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


public class Solution3 {

    public double myPow2(double x, int n) {
        // https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/comments/240095
        if(n == 0) return 1;
        if(n == 1) return x;
        if(n == -1) return 1 / x;
        double half = myPow2(x, n / 2);
        double mod = myPow2(x, n % 2);
        return half * half * mod;
    }

    public double myPow(double x, int n) {
        // 特判，也可以认为是递归终止条件
        long N = n;
        if (N < 0) {
            return 1 / myPow(x, -N);
        }
        return myPow(x, N);
    }

    private double myPow(double x, long n) {
        if (n == 0) {
            return 1;
        }

        if (x == 1) {
            return 1;
        }

        // 根据指数是奇数还是偶数进行分类讨论
        // 使用位运算的 与 运算符代替了求余数运算

        if ((n % 2) == 0) {
            // 分治思想：分
            double square = myPow(x, n / 2);
            // 分治思想：合，下面同理
            return square * square;
        } else {
            // 是奇数的时候
            double square = myPow(x, (n - 1) / 2);
            return square * square * x;
        }
    }

}

// 作者：liweiwei1419
// 链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/di-gui-xie-fa-fen-zhi-si-xiang-yu-fei-di-gui-xie-f/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。