#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
# https://leetcode.cn/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (62.51%)
# Likes:    727
# Dislikes: 0
# Total Accepted:    121.6K
# Total Submissions: 194.4K
# Testcase Example:  '1\n2'
#
# 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。
#
#
#
# 示例 1：
#
#
# 输入：a = 1, b = 2
# 输出：3
#
#
# 示例 2：
#
#
# 输入：a = 2, b = 3
# 输出：5
#
#
#
#
# 提示：
#
#
# -1000 <= a, b <= 1000
#
#
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        # 循环，当进位为 0 时跳出
        while b != 0:
            # a, b = 非进位和, 进位
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)
# @lc code=end

