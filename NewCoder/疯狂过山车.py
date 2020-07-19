# -*- coding: UTF-8 -*-
"""=================================================
Problem:    疯狂过山车
Website: https://ac.nowcoder.com/acm/problem/204898
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""

#
# @param n int整型
# @param num int整型一维数组
# @return int整型
#
class Solution:
    def getMaxLength(self , n , num ):
        # write code here
        if n <= 2:
            return 0
         
        cur = 1
        up = 0
        res = 0
        high = num[0]
        find_up = True
        while cur < n:
            if find_up:
                while num[cur] <= num[cur - 1]:
                    cur += 1
                    if cur >= n:
                        break
                else:
                    up = 2
                    find_up = False
                    cur += 1
            else:
                if num[cur] > num[cur - 1]:
                    up += 1
                    cur += 1
                elif num[cur] == num[cur - 1]:
                    find_up = True
                else:
                    while num[cur] < num[cur - 1]:
                        up += 1
                        cur += 1
                        if cur >= n:
                            res = max(res, up)
                            break
                    else:
                        find_up = True
                        res = max(res, up)
        return res