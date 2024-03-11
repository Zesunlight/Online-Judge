# -*- coding: UTF-8 -*-
"""=================================================
Problem: 299. 猜数字游戏
Website: https://leetcode.cn/problems/bulls-and-cows/description/?envType=daily-question&envId=2024-03-10
Difficulty: 中等
Author: 一朵深渊
Language: Python3
Result: Accepted
Runtime: 42ms
Memory Usage: 16.34MB
=================================================="""
from collections import Counter

'''
你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：

写出一个秘密数字，并请朋友猜这个数字是多少。朋友每猜测一次，你就会给他一个包含下述信息的提示：

猜测数字中有多少位属于数字和确切位置都猜对了（称为 "Bulls"，公牛），
有多少位属于数字猜对了但是位置不对（称为 "Cows"，奶牛）。也就是说，这次猜测中有多少位非公牛数字可以通过重新排列转换成公牛数字。
给你一个秘密数字 secret 和朋友猜测的数字 guess ，请你返回对朋友这次猜测的提示。

提示的格式为 "xAyB" ，x 是公牛个数， y 是奶牛个数，A 表示公牛，B 表示奶牛。

请注意秘密数字和朋友猜测的数字都可能含有重复数字。
'''


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c = Counter(secret)
        a = b = 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                a += 1
                c[secret[i]] -= 1
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                continue
            if c[guess[i]] > 0:
                b += 1
                c[guess[i]] -= 1

        return str(a) + 'A' + str(b) + 'B'

    def getHint2(self, secret: str, guess: str) -> str:
        # https://leetcode.cn/problems/bulls-and-cows/solutions/1088724/cai-shu-zi-you-xi-by-leetcode-solution-q9lz
        bulls = 0
        cntS, cntG = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cntS[int(s)] += 1
                cntG[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(cntS, cntG))
        return f'{bulls}A{cows}B'


if __name__ == '__main__':
    s = Solution()
    print(s.getHint(secret="1807", guess="7810"))
