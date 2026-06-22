class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std:: unordered_set<int> myset(nums.begin(), nums.end());
        int length = myset.size();
        return length != nums.size();
    }
};