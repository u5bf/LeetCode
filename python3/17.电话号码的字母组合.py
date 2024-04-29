#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (59.50%)
# Likes:    2805
# Dislikes: 0
# Total Accepted:    865.9K
# Total Submissions: 1.5M
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#
#
# 示例 1：
#
#
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# 示例 2：
#
#
# 输入：digits = ""
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：digits = "2"
# 输出：["a","b","c"]
#
#
#
#
# 提示：
#
#
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
#
#
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0: return []
        mp = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        ans = []

        def dfs(path, level):
            if level == n:
                ans.append("".join(path))
                return
            for ch in mp[int(digits[level])]:
                path.append(ch)
                dfs(path, level + 1)
                path.pop()

        dfs([], 0)
        return ans


# @lc code=end
