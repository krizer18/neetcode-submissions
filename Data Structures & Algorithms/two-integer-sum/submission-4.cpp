class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std:: unordered_map<int, int> mydict;
        for (int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if (mydict.contains(complement)) {
                return {mydict[complement], i};
            }
            else {
                mydict[nums[i]] = i;
            }
        }
    }
};
