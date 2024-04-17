#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode.cn/problems/partition-list/description/
#
# algorithms
# Medium (64.55%)
# Likes:    826
# Dislikes: 0
# Total Accepted:    270.3K
# Total Submissions: 418.7K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
#
#
# 示例 2：
#
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 200] 内
# -100
# -200
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        new_head = ListNode(0)  # 创建一个新的头节点
        new_head.next = head
        less_x_node = new_head  # 记录小于 x 的节点的前一个节点
        cur_node = head  # 当前节点
        per_node = new_head  # 记录当前节点的前一个节点

        while cur_node:
            if cur_node.val < x:
                if per_node != less_x_node:  # 避免不必要的节点指针操作
                    per_node.next = cur_node.next
                    cur_node.next = less_x_node.next
                    less_x_node.next = cur_node
                    cur_node = per_node.next
                    less_x_node = less_x_node.next
                else:
                    less_x_node = less_x_node.next
                    per_node = per_node.next
                    cur_node = cur_node.next
            else:
                per_node = per_node.next
                cur_node = cur_node.next

        return new_head.next

# @lc code=end

