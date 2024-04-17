#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode.cn/problems/largest-number/description/
#
# algorithms
# Medium (41.00%)
# Likes:    1251
# Dislikes: 0
# Total Accepted:    222.9K
# Total Submissions: 543.7K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#
#
# 示例 1：
#
#
# 输入：nums = [10,2]
# 输出："210"
#
# 示例 2：
#
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
#
#
#
from typing import List
from functools import cmp_to_key
# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums): return "0"
        return "".join(sorted(map(str, nums), key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True))
# @lc code=end

ans = Solution().largestNumber([10, 2])
print(ans)
