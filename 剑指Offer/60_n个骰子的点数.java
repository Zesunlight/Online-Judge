/*
=================================================
Problem: 面试题 60. n个骰子的点数
Website: https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
Difficulty: 简单
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 0 ms, 在所有 Python3 提交中击败了100.00%的用户
Memory Usage: 37.5 MB, 在所有 Python3 提交中击败了91.07%的用户
==================================================*/


class Solution {
    public double[] twoSum(int n) {
        double[] one = new double[] {1/6d, 1/6d, 1/6d, 1/6d, 1/6d, 1/6d};
        if (n == 1) return one;

        double[] pre = twoSum(n - 1);  // n - 1 ... 6 * (n - 1)
        double[] cur = new double[5 * n + 1];  // n ... 6 * n

        for (int i = 0; i < cur.length; i++) {
            for (int j = 0; j < 6; j++) {
                if (i - j >= 0 && i - j < pre.length) cur[i] += one[j] * pre[i - j];
            }
        }

        return cur;
    }
}


class Solution {
    public double[] twoSum(int n) {
        double pre[]={1/6d,1/6d,1/6d,1/6d,1/6d,1/6d};
        for(int i=2;i<=n;i++){
            double tmp[]=new double[5*i+1];
            for(int j=0;j<pre.length;j++)
                for(int x=0;x<6;x++)
                    tmp[j+x]+=pre[j]/6;
            pre=tmp;
        }
        return pre;
    }
}

// 作者：zhi-xiong
// 链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/java-dong-tai-gui-hua-by-zhi-xiong/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


// f(n,s)=f(n-1,s-1)+f(n-1,s-2)+f(n-1,s-3)+f(n-1,s-4)+f(n-1,s-5)+f(n-1,s-6)
