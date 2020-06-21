# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 124. 二叉树中的最大路径和
Website: https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/submissions/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 156 ms, 在所有 Python3 提交中击败了10.09%的用户
Memory Usage: 25.3 MB, 在所有 Python3 提交中击败了20.00%的用户
=================================================="""


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        dp = collections.defaultdict(dict)
        res = root.val
        stack = [root]

        while 1:
            top = stack[-1]
            if 'left' in dp[top] and 'right' in dp[top]:
                temp = top.val
                if dp[top]['left'] > 0:
                    temp += dp[top]['left']
                if dp[top]['right'] > 0:
                    temp += dp[top]['right']
                res = max(res, temp)
                stack.pop()
                if not stack:
                    break

                parent = dp[top]['parent']
                temp = max(dp[top]['left'] + top.val, dp[top]['right'] + top.val, 0)

                if 'left' in dp[parent]:
                    dp[parent]['right'] = temp
                else:
                    dp[parent]['left'] = temp
                continue

            if top.right:
                stack.append(top.right)
                dp[top.right]['parent'] = top
            else:
                dp[top]['right'] = 0
            if top.left:
                stack.append(top.left)
                dp[top.left]['parent'] = top
            else:
                dp[top]['left'] = 0

        return res


class Solution_2:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain
            
            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)
        
            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)
   
        maxGain(root)
        return self.maxSum
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-leetcode-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
