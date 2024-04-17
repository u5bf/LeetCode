#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (50.53%)
# Likes:    1645
# Dislikes: 0
# Total Accepted:    492.2K
# Total Submissions: 973.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1
# -100
#
#
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        ans = []
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            if top > bottom: break

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right: break

            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom: break

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right: break
        return ans

# @lc code=end

#   spiral_order([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# = [1, 2, 3] + spiral_order([[6, 9],
#                             [5, 8],
#                             [4, 7]])

# = [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
#                                      [5, 4]])

# = [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
#                                               [5]])

# = [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

# = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

# = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

# = [1, 2, 3, 6, 9, 8, 7, 4, 5]
