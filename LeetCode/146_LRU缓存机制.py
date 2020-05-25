# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 146. LRU缓存机制
Website: https://leetcode-cn.com/problems/lru-cache/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 3180 ms, 在所有 Python3 提交中击败了5.04%的用户
Memory Usage: 22 MB, 在所有 Python3 提交中击败了65.38%的用户
=================================================="""


class LRUCache:
    """
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
    """

    def __init__(self, capacity: int):
        self.key, self.value = [], []
        self.capacity = capacity

    def get(self, key: int) -> int:
        index = self.find(key)
        if index == -1:
            print(-1)
            return -1
        else:
            temp = self.value[index]
            self.key.pop(index)
            self.value.pop(index)
            self.key.append(key)
            self.value.append(temp)
            print(temp)
            return temp

    def put(self, key: int, value: int) -> None:
        index = self.find(key)
        if index == -1:
            if self.capacity == 0:
                self.key.pop(0)
                self.value.pop(0)
            else:
                self.capacity -= 1

            self.key.append(key)
            self.value.append(value)
        else:
            self.key.pop(index)
            self.value.pop(index)
            self.key.append(key)
            self.value.append(value)

    def find(self, key):
        for i in range(len(self.key)):
            if self.key[i] == key:
                return i
        else:
            return -1


cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
cache.get(1)
cache.get(2)
cache.get(4)


"""
https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/
https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/

LRU 缓存机制可以通过哈希表辅以双向链表实现，我们用一个哈希表和一个双向链表维护所有在缓存中的键值对。

双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。

哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。

这样以来，我们首先使用哈希表进行定位，找出缓存项在双向链表中的位置，随后将其移动到双向链表的头部，即可在 O(1) O(1) 的时间内完成 get 或者 put 操作。

在双向链表的实现中，使用一个伪头部（dummy head）和伪尾部（dummy tail）标记界限，这样在添加节点和删除节点的时候就不需要检查相邻的节点是否存在。

"""