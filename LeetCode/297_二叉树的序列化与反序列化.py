# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 297. 二叉树的序列化与反序列化
Website: https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 260 ms, 在所有 Python3 提交中击败了13.21%的用户
Memory Usage: 34 MB, 在所有 Python3 提交中击败了12.50%的用户
=================================================="""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
    同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

    请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
    你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            top = q.popleft()
            if top is None:
                res.append(None)
                continue
            res.append(top.val)
            q.append(top.left)
            q.append(top.right)
        return repr(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = eval(data)
        if l == []:
            return None
        root = TreeNode(l.pop(0))
        q = collections.deque()
        q.append(root)
        while l:
            top = q.popleft()
            left_val = l.pop(0)
            if left_val is not None:
                top.left = TreeNode(left_val)
                q.append(top.left)
            if l:
                right_val = l.pop(0)
                if right_val is not None:
                    top.right = TreeNode(right_val)
                    q.append(top.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

'''
public class Codec {
    public String rserialize(TreeNode root, String str) {
        if (root == null) {
            str += "None,";
        } else {
            str += str.valueOf(root.val) + ",";
            str = rserialize(root.left, str);
            str = rserialize(root.right, str);
        }
        return str;
    }
  
    public String serialize(TreeNode root) {
        return rserialize(root, "");
    }
  
    public TreeNode rdeserialize(List<String> l) {
        if (l.get(0).equals("None")) {
            l.remove(0);
            return null;
        }
  
        TreeNode root = new TreeNode(Integer.valueOf(l.get(0)));
        l.remove(0);
        root.left = rdeserialize(l);
        root.right = rdeserialize(l);
    
        return root;
    }
  
    public TreeNode deserialize(String data) {
        String[] data_array = data.split(",");
        List<String> data_list = new LinkedList<String>(Arrays.asList(data_array));
        return rdeserialize(data_list);
    }
};

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/er-cha-shu-de-xu-lie-hua-yu-fan-xu-lie-hua-by-le-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''