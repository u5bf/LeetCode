#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Medium (60.04%)
# Likes:    1183
# Dislikes: 0
# Total Accepted:    670.2K
# Total Submissions: 1.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target
# 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <=
# numbers.length 。
#
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
#
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
#
# 你所设计的解决方案必须只使用常量级的额外空间。
#
#
# 示例 1：
#
#
# 输入：numbers = [2,7,11,15], target = 9
# 输出：[1,2]
# 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
#
# 示例 2：
#
#
# 输入：numbers = [2,3,4], target = 6
# 输出：[1,3]
# 解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
#
# 示例 3：
#
#
# 输入：numbers = [-1,0], target = -1
# 输出：[1,2]
# 解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
#
#
#
#
# 提示：
#
#
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers 按 非递减顺序 排列
# -1000 <= target <= 1000
# 仅存在一个有效答案
#
#
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if (ans := numbers[i] + numbers[j]) > target:
                j -= 1
            elif ans < target:
                i += 1
            else:
                return [i + 1, j + 1]
        return [0, 0] # 不会执行到这，因为确保有一个解,而且是唯一解
# @lc code=end

