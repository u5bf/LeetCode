#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode.cn/problems/group-anagrams/description/
#
# algorithms
# Medium (67.93%)
# Likes:    1864
# Dislikes: 0
# Total Accepted:    672.8K
# Total Submissions: 990K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
#
#
#
# 示例 1:
#
#
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# 示例 2:
#
#
# 输入: strs = [""]
# 输出: [[""]]
#
#
# 示例 3:
#
#
# 输入: strs = ["a"]
# 输出: [["a"]]
#
#
#
# 提示：
#
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母
#
#
#
from collections import defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)
        return list(letters_to_words.values())
# @lc code=end

