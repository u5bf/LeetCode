#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode.cn/problems/minimum-window-substring/description/
#
# algorithms
# Hard (45.60%)
# Likes:    2872
# Dislikes: 0
# Total Accepted:    548.7K
# Total Submissions: 1.2M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
# 。
#
#
#
# 注意：
#
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
#
#
# 示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
#
#
# 示例 3:
#
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
#
# 提示：
#
#
# ^m == s.length
# ^n == t.length
# 1 <= m, n <= 10^5
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
#
from collections import defaultdict, Counter
# @lc code=start
class Solution:
    # 思路来源 https://www.bilibili.com/video/BV15S4y1U767/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=a37fef91b4c498111cd2a59d58e5a625
    def minWindow(self, s: str, t: str) -> str:
        hs, ht = defaultdict(int), Counter(t)
        ans = ""
        cnt = 0
        i = j = 0
        lens, lent = len(s), len(t)
        while j < lens:
            hs[s[j]] += 1
            if hs[s[j]] <= ht[s[j]]:
                cnt += 1
            j += 1
            while i < lens and hs[s[i]] > ht[s[i]]:
                hs[s[i]] -= 1
                i += 1
            if cnt == lent and len(ans) == 0 or len(ans) > j - i:
                ans = s[i:j]
        return ans
# @lc code=end
