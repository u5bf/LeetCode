#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode.cn/problems/longest-palindrome/description/
#
# algorithms
# Easy (55.68%)
# Likes:    587
# Dislikes: 0
# Total Accepted:    195.5K
# Total Submissions: 351.2K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。
#
# 在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。
#
#
#
# 示例 1:
#
#
# 输入:s = "abccccdd"
# 输出:7
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#
#
# 示例 2:
#
#
# 输入:s = "a"
# 输出:1
#
#
# 示例 3：
#
#
# 输入:s = "aaaaaccc"
# 输出:7
#
#
#
# 提示:
#
#
# 1 <= s.length <= 2000
# s 只由小写 和/或 大写英文字母组成
#
#
#
import collections
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = collections.Counter(s)
        center = sum(1 for count in dic.values() if count & 1 == 1)
        return len(s) - center + (center > 0)
# @lc code=end

