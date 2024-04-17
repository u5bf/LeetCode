#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode.cn/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (71.15%)
# Likes:    1271
# Dislikes: 0
# Total Accepted:    409.3K
# Total Submissions: 575.5K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：[[1]]
#
#
#
#
# 提示：
#
#
# 1
#
#
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = left = 0
        bottom, right = n - 1, n - 1
        matrix = [[0] * n for _ in range(n)]
        num = 1
        while True:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            if top > bottom: break

            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if left > right: break

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            if top > bottom: break

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            if left > right: break
        return matrix
# @lc code=end

