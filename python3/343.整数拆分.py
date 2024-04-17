#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode.cn/problems/integer-break/description/
#
# algorithms
# Medium (63.11%)
# Likes:    1361
# Dislikes: 0
# Total Accepted:    321.6K
# Total Submissions: 509.2K
# Testcase Example:  '2'
#
# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
#
# 返回 你可以获得的最大乘积 。
#
#
#
# 示例 1:
#
#
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
#
# 示例 2:
#
#
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
#
#
#
# 提示:
#
#
# 2 <= n <= 58
#
#
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n-1
        k = n // 3
        r = n % 3
        ans = 3**k
        if r == 1: ans = ans // 3 * 4
        if r == 2: ans *= 2
        return ans
# @lc code=end

