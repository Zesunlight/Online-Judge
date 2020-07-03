# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 108. 将有序数组转换为二叉搜索树
Website: https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 68 ms, 在所有 Python3 提交中击败了25.02%的用户
Memory Usage: 15.8 MB, 在所有 Python3 提交中击败了9.52%的用户
=================================================="""


class Solution:
    """
    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    本题中，一棵高度平衡二叉树定义为：
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l = len(nums)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(nums[0])
        
        root = TreeNode(nums[l // 2])
        root.left = self.sortedArrayToBST(nums[:l // 2])
        root.right = self.sortedArrayToBST(nums[l // 2 + 1:])
        return root

    def sortedArrayToBST_2(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 选择任意一个中间位置数字作为根节点
            mid = (left + right + randint(0, 1)) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)
    """
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/jiang-you-xu-shu-zu-zhuan-huan-wei-er-cha-sou-s-33/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
