#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode.cn/problems/regular-expression-matching/description/
#
# algorithms
# Hard (30.70%)
# Likes:    3865
# Dislikes: 0
# Total Accepted:    411.9K
# Total Submissions: 1.3M
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
#
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
#
# 示例 1：
#
#
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#
#
# 示例 2:
#
#
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
# 示例 3：
#
#
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符
#
#
#

# @lc code=start
class Solution:
    # 思路来源 https://www.bilibili.com/video/BV13441117i4?p=1&vd_source=a37fef91b4c498111cd2a59d58e5a625
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(2, m+1):
            dp[0][j] = p[j-1] == "*" and dp[0][j-2]

        def match(i, j):
            return s[i] == p[j] or p[j] == "."

        for i in range(n):
            for j in range(m):
                if p[j] == "*":
                    dp[i+1][j+1] = dp[i+1][j-1] or match(i, j-1) and dp[i][j+1]
                else:
                    dp[i+1][j+1] = match(i,j) and dp[i][j]
        return dp[n][m]
# @lc code=end
