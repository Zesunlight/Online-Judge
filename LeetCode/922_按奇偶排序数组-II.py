# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 922. 按奇偶排序数组 II
Website: https://leetcode-cn.com/problems/sort-array-by-parity-ii/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 304 ms, 在所有 Python3 提交中击败了16.60%的用户
Memory Usage: 15.9 MB, 在所有 Python3 提交中击败了11.14%的用户
=================================================="""


class Solution:
    '''
    你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
    你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
    '''
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        B = [0] * len(A)
        A.sort()
        odd, even = 1, 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                B[even] = A[i]
                even += 2
            else:
                B[odd] = A[i]
                odd += 2
        return B


'''
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int n = A.length;
        int j = 1;
        for (int i = 0; i < n; i += 2) {
            if (A[i] % 2 == 1) {
                while (A[j] % 2 == 1) {
                    j += 2;
                }
                swap(A, i, j);
            }
        }   
        return A;
    }

    public void swap(int[] A, int i, int j) {
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii/solution/an-qi-ou-pai-xu-shu-zu-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
