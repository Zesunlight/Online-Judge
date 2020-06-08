# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 手机屏幕解锁模式（vivo2020届春季校园招聘在线编程考试）
Website: https://www.nowcoder.com/question/next?pid=22390442&qid=925106&tid=32281691
Author: ZYZ
Language: Python3
Result: 
=================================================="""

# 现有一个 3x3 规格的 Android 智能手机锁屏程序和两个正整数 m 和 n ，请计算出使用最少m 个键和最多 n个键可以解锁该屏幕的所有有效模式总数。
# 其中有效模式是指：
# 1、每个模式必须连接至少m个键和最多n个键；
# 2、所有的键都必须是不同的；
# 3、如果在模式中连接两个连续键的行通过任何其他键，则其他键必须在模式中选择，不允许跳过非选择键（如图）；
# 4、顺序相关，单键有效（这里可能跟部分手机不同）。

from itertools import chain, permutations

class Solution:
    # https://github.com/15757170756/All-Code-I-Have-Done/blob/ac8bd01e353039bb8072540eb8efbc4bfbb3263e/%E7%89%9B%E5%AE%A2%E7%BD%91%E5%90%84%E7%B1%BB%E7%AC%94%E8%AF%95%E9%A2%98%E7%9B%AE/vivo2020%E5%B1%8A%E6%98%A5%E5%AD%A3%E6%A0%A1%E5%9B%AD%E6%8B%9B%E8%81%98%E5%9C%A8%E7%BA%BF%E7%BC%96%E7%A8%8B%E8%80%83%E8%AF%95/%5B%E7%BC%96%E7%A8%8B%E9%A2%98%5D%E6%89%8B%E6%9C%BA%E5%B1%8F%E5%B9%95%E8%A7%A3%E9%94%81%E6%A8%A1%E5%BC%8F.py
    impossible = {'13': '2',
                  '46': '5',
                  '79': '8',
                  '17': '4',
                  '28': '5',
                  '39': '6',
                  '19': '5',
                  '37': '5',
                  '31': '2',
                  '64': '5',
                  '97': '8',
                  '71': '4',
                  '82': '5',
                  '93': '6',
                  '91': '5',
                  '73': '5'}
    def solution(self , m , n ):
        if m == 0 and n == 0:
            return 0
        if m == 0:
            m += 1
        iterlst = chain(*(permutations('123456789', i) for i in range(m, n+1)))
        count = 0
        for i in iterlst:
            stri = ''.join(i)
            for k, v in self.impossible.items():
                if k in stri and v not in stri[:stri.find(k)]:
                    break
            else:
                count += 1
        return count
