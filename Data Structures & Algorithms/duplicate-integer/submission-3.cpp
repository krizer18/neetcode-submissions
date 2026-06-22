class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> myset(nums.begin(), nums.end());
        int mysetsize = myset.size();
        return !(myset.size() == nums.size());
    }
};