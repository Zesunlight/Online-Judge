# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题37. 序列化二叉树
Website: https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 160 ms, 在所有 Python3 提交中击败了58.86%的用户
Memory Usage: 26.2 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    请实现两个函数，分别用来序列化和反序列化二叉树。
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = deque()
        if root:
            q.append(root)
        else:
            # 特殊情况
            return '[]'

        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)

        end = len(res) - 1
        while res[end] is None:
            end -= 1
        return repr(res[:end+1]).replace("None", "null")


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = eval(data.replace("null", "None"))
        if (not res) or res[0] is None:
            return None
        q = deque()
        root = TreeNode(res[0])
        q.append(root)
        for i in range(1, len(res), 2):
            node = q.popleft()
            if res[i] is not None:
                # 注意判断条件，写完整
                # 若采用 if res[i] ，当 res[i]=0 时有错误
                node.left = TreeNode(res[i])
                q.append(node.left)
            if i + 1 < len(res) and res[i + 1] is not None:
                # 注意边界情况
                node.right = TreeNode(res[i + 1])
                q.append(node.right)
        return root


from collections import deque
c = Codec()
print(c.serialize(c.deserialize("[-1,0,1]")))


"""
class Codec:
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

作者：jyd
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/solution/mian-shi-ti-37-xu-lie-hua-er-cha-shu-ceng-xu-bian-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
