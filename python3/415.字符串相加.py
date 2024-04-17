#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode.cn/problems/add-strings/description/
#
# algorithms
# Easy (54.54%)
# Likes:    818
# Dislikes: 0
# Total Accepted:    323.3K
# Total Submissions: 592.9K
# Testcase Example:  '"11"\n"123"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
#
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
#
#
#
# 示例 1：
#
#
# 输入：num1 = "11", num2 = "123"
# 输出："134"
#
#
# 示例 2：
#
#
# 输入：num1 = "456", num2 = "77"
# 输出："533"
#
#
# 示例 3：
#
#
# 输入：num1 = "0", num2 = "0"
# 输出："0"
#
#
#
#
#
#
# 提示：
#
#
# 1 <= num1.length, num2.length <= 10^4
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
#
#
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        n1, n2 = len(num1), len(num2)
        zero = ord("0")
        if n1 < n2:
            num1, num2 = num2, num1
            n1, n2 = n2, n1
        up_bit = 0
        for a, b in zip(num1[::-1], num2[::-1]):
            tmp = ord(a) - zero + ord(b) - zero + up_bit
            up_bit = tmp // 10
            tmp %= 10
            ans = chr(tmp + zero) + ans

        # 处理 num1 剩余的高位数字
        for a in num1[:n1-n2][::-1]:
            tmp = ord(a) - zero + up_bit
            up_bit = tmp // 10
            tmp %= 10
            ans = chr(tmp + zero) + ans

        # 处理最高位的进位
        if up_bit > 0:
            ans = chr(up_bit + zero) + ans
        return ans
# @lc code=end

ans = Solution().addStrings("9", "99")
print(ans)
