/*
 * @lc app=leetcode.cn id=79 lang=cpp
 *
 * [79] 单词搜索
 *
 * https://leetcode.cn/problems/word-search/description/
 *
 * algorithms
 * Medium (46.88%)
 * Likes:    1806
 * Dislikes: 0
 * Total Accepted:    518.3K
 * Total Submissions: 1.1M
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false
 * 。
 *
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
 * "ABCCED"
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
 * "SEE"
 * 输出：true
 *
 *
 * 示例 3：
 *
 *
 * 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
 * "ABCB"
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == board.length
 * n = board[i].length
 * 1
 * 1
 * board 和 word 仅由大小写英文字母组成
 *
 *
 *
 *
 * 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
 *
 */

// @lc code=start
class Solution {
    int m;
    int n;
    int word_size;

    bool dfs(vector<vector<char>>& board, string const& word, int p, int i, int j) {
        if (p == word_size) return true;
        if (0 > i || 0 > j || i >= m || j >= n || board[i][j] != word[p]) return false;
        board[i][j] = '#';
        auto up = dfs(board, word, p + 1, i - 1, j);
        auto down = dfs(board, word, p + 1, i + 1, j);
        auto left = dfs(board, word, p + 1, i, j - 1);
        auto right = dfs(board, word, p + 1, i, j + 1);
        board[i][j] = word[p];
        return up || down || left || right;
    }
    
public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();
        word_size = word.size();

        for (int i{}; i < m; ++i) {
            for (int j{}; j < n; ++j) {
                if (dfs(board, word, 0, i, j)) {
                    return true;
                }
            }
        }
        return false;
    }
};
// @lc code=end

