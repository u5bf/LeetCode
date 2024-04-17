#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (53.63%)
# Likes:    1416
# Dislikes: 0
# Total Accepted:    411.1K
# Total Submissions: 767.8K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#
#
#
# 示例 1:
#
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#
#
# 示例 2:
#
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
#
#
# 提示:
#
#
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母
#
#
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1

            if differ == 0:
                ans.append(i + 1)

        return ans
# @lc code=end

