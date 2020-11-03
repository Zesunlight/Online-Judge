/*
    941. 有效的山脉数组
    https://leetcode-cn.com/problems/valid-mountain-array/

    给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

    让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

    A.length >= 3
    在 0 < i < A.length - 1 条件下，存在 i 使得：
    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[A.length - 1]

    执行用时：3 ms, 在所有 Java 提交中击败了11.40%的用户
    内存消耗：39.9 MB, 在所有 Java 提交中击败了9.79%的用户
 */


class Solution {
    public boolean validMountainArray(int[] A) {
        if (A.length < 3) {
            return false;
        }
        if (A[1] <= A[0]) {
            return false;
        }
        boolean increase = true;
        for (int i = 1; i < A.length; i++) {
            if (i < A.length - 1 && A[i] == A[i + 1]) {
                return false;
            }
            if (i < A.length - 1 && !increase && A[i] <= A[i + 1]) {
                return false;
            }
            if (increase && A[i] < A[i - 1]) {
                increase = false;
                if (i < A.length - 1 && A[i] <= A[i + 1]) {
                    return false;
                }
            }
        }
        return !increase;
    }

    public boolean validMountainArray2(int[] A) {
        int len = A.length;
        int left = 0;
        int right = len - 1;
        //从左边往右边找，一直找到山峰为止
        while (left + 1 < len && A[left] < A[left + 1])
            left++;
        //从右边往左边找，一直找到山峰为止
        while (right > 0 && A[right - 1] > A[right])
            right--;
        //判断从左边和从右边找的山峰是不是同一个
        return left > 0 && right < len - 1 && left == right;
    }

    // 作者：sdwwld
    // 链接：https://leetcode-cn.com/problems/valid-mountain-array/solution/shuang-zhi-zhen-ji-bai-liao-100de-yong-hu-by-sdwwl/
    // 来源：力扣（LeetCode）
    // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
}


class Solution2 {
    public boolean validMountainArray(int[] A) {
        int N = A.length;
        int i = 0;

        // 递增扫描
        while (i + 1 < N && A[i] < A[i + 1]) {
            i++;
        }

        // 最高点不能是数组的第一个位置或最后一个位置
        if (i == 0 || i == N - 1) {
            return false;
        }

        // 递减扫描
        while (i + 1 < N && A[i] > A[i + 1]) {
            i++;
        }

        return i == N - 1;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/valid-mountain-array/solution/you-xiao-de-shan-mai-shu-zu-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。