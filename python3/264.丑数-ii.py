#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode.cn/problems/ugly-number-ii/description/
#
# algorithms
# Medium (58.25%)
# Likes:    1168
# Dislikes: 0
# Total Accepted:    173.1K
# Total Submissions: 297.2K
# Testcase Example:  '10'
#
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
#
# 丑数 就是质因子只包含 2、3 和 5 的正整数。
#
#
#
# 示例 1：
#
#
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#
#
#
#
# 提示：
#
#
# 1 <= n <= 1690
#
#
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 思路来源 https://www.bilibili.com/video/BV1o541177He/?spm_id_from=333.1007.top_right_bar_window_history.content.click
        # if n < 7: return n # 简单的情况直接返回
        dp = [1] * n
        p2 = p3 = p5 = 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2: p2 += 1
            if dp[i] == dp[p3] * 3: p3 += 1
            if dp[i] == dp[p5] * 5: p5 += 1
        return dp[-1]
# @lc code=end
