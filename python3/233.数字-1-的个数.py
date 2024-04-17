#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# https://leetcode.cn/problems/number-of-digit-one/description/
#
# algorithms
# Hard (49.37%)
# Likes:    577
# Dislikes: 0
# Total Accepted:    63.2K
# Total Submissions: 127.9K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
#
#
# 示例 1：
#
#
# 输入：n = 13
# 输出：6
#
#
# 示例 2：
#
#
# 输入：n = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= n <= 10^9
#
#
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        # mulk 表示 10^k
        # 在下面的代码中，可以发现 k 并没有被直接使用到（都是使用 10^k）
        # 但为了让代码看起来更加直观，这里保留了 k
        k, mulk = 0, 1
        ans = 0
        while n >= mulk:
            ans += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0), mulk)
            k += 1
            mulk *= 10
        return ans
# @lc code=end

