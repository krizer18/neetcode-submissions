class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<vector<int>> result;

        for (int i = 0; i < nums.size() - 1; i++) {

            if (nums[i] > 0) {
                break;
            }

            if (i > 0 and nums[i] == nums[i - 1]){
                continue;
            }

            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r) {
                int tsum = nums[i] + nums[l] + nums[r];
                if (tsum > 0) {
                    r -= 1;
                }
                else if (tsum < 0) {
                    l += 1;
                }
                else {
                    vector<int> myvect = {nums[i], nums[l], nums[r]};
                    result.push_back(myvect);
                    l += 1;
                    r -= 1;
                    while (nums[l] == nums[l - 1] and l < r) {
                        l += 1;
                    }
                }
            }
        }
        return result;
    }
};
