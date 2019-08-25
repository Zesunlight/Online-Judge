"""
    Problem: 48. Rotate Image
    Website: https://leetcode.com/problems/rotate-image/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 40 ms, faster than 82.56% of Python3 online submissions for Rotate Image.
    Memory Usage: 13.5 MB, less than 6.25% of Python3 online submissions for Rotate Image.
"""


class Solution:
    """
    You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

    Note:

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation.
    """

    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        import copy

        temp = copy.deepcopy(matrix)
        # 分配了空间，其实不符题意
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[j][-i - 1] = temp[i][j]


s = Solution()
a = [[5, 1, 9, 11],
     [2, 4, 8, 10],
     [13, 3, 6, 7],
     [15, 14, 12, 16]]
s.rotate(a)
print(a)


"""
https://leetcode.com/problems/rotate-image/discuss/18888/1-line-in-Python

# 先把矩阵上下翻转，然后在转置一下
matrix[::] = zip(*matrix[::-1])

# Rotate the image by 90 degrees (anticlockwise)
# 先把矩阵转置一下，然后在上下翻转
matrix[::] = zip(*matrix)[::-1]
"""

"""
https://leetcode.com/problems/rotate-image/discuss/18879/AC-Java-in-place-solution-with-explanation-Easy-to-understand.
The idea was firstly transpose the matrix and then flip it symmetrically. 

public class Solution {
    public void rotate(int[][] matrix) {
        for(int i = 0; i<matrix.length; i++){
            for(int j = i; j<matrix[0].length; j++){
                int temp = 0;
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(int i =0 ; i<matrix.length; i++){
            for(int j = 0; j<matrix.length/2; j++){
                int temp = 0;
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix.length-1-j];
                matrix[i][matrix.length-1-j] = temp;
            }
        }
    }
}
"""

"""
https://leetcode.com/problems/rotate-image/discuss/19002/4ms-few-lines-C++-code-Rotate-Image-90-degree-for-O(1)-space

void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int a = 0;
        int b = n-1;
        while(a<b){
            for(int i=0;i<(b-a);++i){
                swap(matrix[a][a+i], matrix[a+i][b]);
                swap(matrix[a][a+i], matrix[b][b-i]);
                swap(matrix[a][a+i], matrix[b-i][a]);
            }
            ++a;
            --b;
        }
    }
"""