#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#
# https://leetcode.cn/problems/nth-digit/description/
#
# algorithms
# Medium (45.57%)
# Likes:    402
# Dislikes: 0
# Total Accepted:    63.1K
# Total Submissions: 138.4K
# Testcase Example:  '3'
#
# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n
# 位上的数字。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：3
#
#
# 示例 2：
#
#
# 输入：n = 11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
#
#
#
#
# 提示：
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2.
        return int(str(num)[(n - 1) % digit]) # 3.
# @lc code=end

