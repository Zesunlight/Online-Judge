# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1028. 从先序遍历还原二叉树
Website: https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 100 ms, 在所有 Python3 提交中击败了38.03%的用户
Memory Usage: 14.1 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    我们从二叉树的根节点 root 开始进行深度优先搜索。

    在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。
    （如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

    如果节点只有一个子节点，那么保证该子节点为左子节点。

    给出遍历输出 S，还原树并返回其根节点 root。
    """
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        stack = []
        pre_depth = -1
        pre_node = None
        while i < len(S):
            depth = 0
            while S[i] == '-':
                depth += 1
                i += 1
            value = ''
            while i < len(S) and S[i].isdigit():
                value += S[i]
                i += 1
            node = TreeNode(int(value))
            
            if stack and depth == pre_depth + 1:
                stack[-1].left = node
            else:
                for _ in range(pre_depth - depth + 1):
                    stack.pop()
                if stack:
                    stack[-1].right = node
            pre_depth = depth
            stack.append(node)
        return stack[0]


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        path, pos = list(), 0
        while pos < len(S):
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(S) and S[pos].isdigit():
                value = value * 10 + (ord(S[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/solution/cong-xian-xu-bian-li-huan-yuan-er-cha-shu-by-leetc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''