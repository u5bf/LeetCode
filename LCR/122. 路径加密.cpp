#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string pathEncryption(string path) {
        for (auto& v:path) {
            if (v == '.') {
                v = ' ';
            }
        }
        return path;
    }
};

int main(int argc, char const *argv[])
{
    std::cin.tie(nullptr)->std::ios::sync_with_stdio(false);
    Solution();
    return 0;
}

