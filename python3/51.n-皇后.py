#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode.cn/problems/n-queens/description/
#
# algorithms
# Hard (73.93%)
# Likes:    2069
# Dislikes: 0
# Total Accepted:    394.3K
# Total Submissions: 533.4K
# Testcase Example:  '4'
#
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
#
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：[["Q"]]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 9
#
#
#
#
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = [["." for _ in range(n)] for _ in range(n)]
        cols = [False] * n  # 记录列是否有皇后
        diags1 = [False] * (2 * n - 1)  # 记录主对角线上是否有皇后
        diags2 = [False] * (2 * n - 1)  # 记录次对角线上是否有皇后
        ans = []

        def backtrack(i):
            if i == n:
                ans.append(["".join(row) for row in state])
                return

            for j in range(n):
                if not cols[j] and not diags1[i - j + n - 1] and not diags2[i + j]:
                    state[i][j] = "Q"
                    cols[j] = diags1[i - j + n - 1] = diags2[i + j] = True
                    backtrack(i + 1)
                    state[i][j] = "."
                    cols[j] = diags1[i - j + n - 1] = diags2[i + j] = False

        backtrack(0)
        return ans


# @lc code=end
