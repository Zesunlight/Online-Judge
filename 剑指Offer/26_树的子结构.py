# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题26. 树的子结构
Website: https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 112 ms, 在所有 Python3 提交中击败了90.28%的用户
Memory Usage: 18.2 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
    B是A的子结构， 即 A中有出现和B相同的结构和节点值。
    """
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None or A is None:
            return False
        elif A.val == B.val:
            return self.isSame(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        else:
            return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        
    def isSame(self, A, B):
        if B is None:
            return True
        elif A is None:
            return False
        elif A.val == B.val:
            return self.isSame(A.left, B.left) and self.isSame(A.right, B.right)
        else:
            return False

"""
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

作者：jyd
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/mian-shi-ti-26-shu-de-zi-jie-gou-xian-xu-bian-li-p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
