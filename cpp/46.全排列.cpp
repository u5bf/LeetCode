/*
 * @lc app=leetcode.cn id=46 lang=cpp
 *
 * [46] 全排列
 *
 * https://leetcode.cn/problems/permutations/description/
 *
 * algorithms
 * Medium (79.16%)
 * Likes:    2874
 * Dislikes: 0
 * Total Accepted:    1.1M
 * Total Submissions: 1.3M
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,1]
 * 输出：[[0,1],[1,0]]
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1]
 * 输出：[[1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * nums 中的所有整数 互不相同
 *
 *
 */

// @lc code=start
class Solution {
    vector<vector<int>> ans;

    void dfs(vector<int>& nums, int level, int size) {
        if (level == size) {
            this->ans.push_back(nums);
            return;
        }
        for (int i = level; i < size; ++i) {
            swap(nums[i], nums[level]);
            dfs(nums, level + 1, size);
            swap(nums[i], nums[level]);
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int size = nums.size();
        dfs(nums, 0, size);
        return this->ans;
    }
};
// @lc code=end

