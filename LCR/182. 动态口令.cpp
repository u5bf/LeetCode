#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string dynamicPassword(string password, int target) {
        reverse(password.begin(), password.begin() + target);
        reverse(password.begin() + target, password.end());
        reverse(password.begin(), password.end());
        return password; // return password.substr(target) + password.substr(0, target);
    }
};

int main(int argc, char const *argv[])
{
    std::cin.tie(nullptr)->std::ios::sync_with_stdio(false);
    Solution();
    return 0;
}

