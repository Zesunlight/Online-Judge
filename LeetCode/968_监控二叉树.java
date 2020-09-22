/*
    968. 监控二叉树
    https://leetcode-cn.com/problems/binary-tree-cameras/

    给定一个二叉树，我们在树的节点上安装摄像头。
    节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
    计算监控树的所有节点所需的最小摄像头数量。

    执行用时：1 ms, 在所有 Java 提交中击败了55.79%的用户
    内存消耗：38.3 MB, 在所有 Java 提交中击败了93.92%的用户
 */


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int minCameraCover(TreeNode root) {
        if (root == null) return 0;
        int[] array = dfs(root);
        return Math.min(array[0], array[1]);
    }

    public int[] dfs(TreeNode root) {
        // 根有，覆盖全部；根无，覆盖全部；根无，覆盖左右子树
        if (root.left == null & root.right == null) {
            return new int[] {1, 1, 0};
        } else if (root.left == null) {
            int[] rightArray = dfs(root.right);
            return new int[] {1 + rightArray[2], rightArray[0], Math.min(rightArray[0], rightArray[1])};
        } else if (root.right == null) {
            int[] leftArray = dfs(root.left);
            return new int[] {1 + leftArray[2], leftArray[0], Math.min(leftArray[0], leftArray[1])};
        } else {
            int[] rightArray = dfs(root.right);
            int[] leftArray = dfs(root.left);
            int[] array = new int[3];
            array[0] = Math.min(leftArray[0], Math.min(leftArray[1], leftArray[2])) +
                       Math.min(rightArray[0], Math.min(rightArray[1], rightArray[2])) + 1;
            array[1] = Math.min(leftArray[0] + rightArray[0],
                       Math.min(leftArray[0] + rightArray[1], leftArray[1] + rightArray[0]));
            array[2] = Math.min(leftArray[0], leftArray[1]) + Math.min(rightArray[0], rightArray[1]);
            return array;
        }
    }
}


class Solution2 {
    public int minCameraCover(TreeNode root) {
        int[] array = dfs(root);
        return array[1];
    }

    public int[] dfs(TreeNode root) {
        // 状态 a：root 必须放置摄像头的情况下，覆盖整棵树需要的摄像头数目。
        // 状态 b：覆盖整棵树需要的摄像头数目，无论 root 是否放置摄像头。
        // 状态 c：覆盖两棵子树需要的摄像头数目，无论节点 root 本身是否被监控到。

        if (root == null) {
            return new int[]{Integer.MAX_VALUE / 2, 0, 0};
        }
        int[] leftArray = dfs(root.left);
        int[] rightArray = dfs(root.right);
        int[] array = new int[3];
        array[0] = leftArray[2] + rightArray[2] + 1;
        array[1] = Math.min(array[0], Math.min(leftArray[0] + rightArray[1], rightArray[0] + leftArray[1]));
        array[2] = Math.min(array[0], leftArray[1] + rightArray[1]);
        return array;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/binary-tree-cameras/solution/jian-kong-er-cha-shu-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


// https://leetcode-cn.com/problems/binary-tree-cameras/solution/chao-ji-hao-li-jie-de-da-an-by-levyjeng/601450
class Solution3 {
    int res=0;
    public int minCameraCover(TreeNode root) {
        if(dfs(root)==0){
            res++;
        }
        return res;

    }
    /*
    dfs返回节点的状态
    0:未被摄像头照到（覆盖）
    1：被摄像头照到（覆盖）
    2：放置了摄像头
    
    */
    public int dfs(TreeNode root){
        /*为了保证摄像头数目最小，叶子节点不能放置摄像头。
        所以root是null时，设置其状态是已覆盖。*/
        if(root==null){
            return 1;
        }
        
        int left=dfs(root.left);
        int right=dfs(root.right);
        // 左右孩子一共有 00,01,02,11,12,22 这些状态
        
        
        // 包含了 00 01 02 状态，左右孩子只要有一个未被覆盖，root就需要放置摄像头
        if(left==0||right==0){
            res++;
            return 2;
        }
        
        // 11状态  root需要被父节点的摄像头覆盖，设置root的状态是0
        if(left==1&&right==1){
            return 0;    
        }
        
        //12 22状态，root被儿子覆盖 设置root的状态是1
        if(left+right>=3){
            return  1;
        }
        
        // 所有的状态都已经被包含，这里随便返回一个值
        return 0;
        
    }
}
