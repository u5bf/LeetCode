#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode.cn/problems/isomorphic-strings/description/
#
# algorithms
# Easy (49.33%)
# Likes:    705
# Dislikes: 0
# Total Accepted:    259.1K
# Total Submissions: 525.1K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t ，判断它们是否是同构的。
#
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
#
#
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
#
#
#
# 示例 1:
#
#
# 输入：s = "egg", t = "add"
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "foo", t = "bar"
# 输出：false
#
# 示例 3：
#
#
# 输入：s = "paper", t = "title"
# 输出：true
#
#
#
# 提示：
#
#
#
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s 和 t 由任意有效的 ASCII 字符组成
#
#
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            # 对于已有映射 a -> s2t[a]，若和当前字符映射 a -> b 不匹配，
            # 说明有一对多的映射关系，则返回 false ；
            # 对于映射 b -> a 也同理
            if a in s2t and s2t[a] != b or \
               b in t2s and t2s[b] != a:
                return False
            s2t[a], t2s[b] = b, a
        return True
# @lc code=end

ans = Solution().isIsomorphic("badc", "baba")
print(ans)
