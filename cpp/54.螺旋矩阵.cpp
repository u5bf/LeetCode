/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode.cn/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (50.53%)
 * Likes:    1645
 * Dislikes: 0
 * Total Accepted:    492.2K
 * Total Submissions: 973.7K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,2,3,6,9,8,7,4,5]
 *
 *
 * 示例 2：
 *
 *
 * 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1
 * -100
 *
 *
 */

// @lc code=start
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int left = 0;
        int right = matrix[0].size() - 1;
        int top = 0;
        int bottom = matrix.size() - 1;
        vector<int> ans;
        ans.reserve(matrix[0].size() * matrix.size());
        for (;;) {
            for (int i = left; i <= right; ++i) {
                ans.push_back(matrix[top][i]);
            }
            if (++top > bottom) break;

            for (int i = top; i <= bottom; ++i) {
                ans.push_back(matrix[i][right]);
            }
            if (--right < left) break;

            for (int i = right; i >= left; --i) {
                ans.push_back(matrix[bottom][i]);
            }
            if (--bottom < top) break;

            for (int i = bottom; i >= top; --i) {
                ans.push_back(matrix[i][left]);
            }
            if (++left > right) break;
        }
        return ans;
    }
};
// @lc code=end

