class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<vector<int>> res(nums.size() + 1);
        std::unordered_map<int, int> count;

        for (int i = 0; i < nums.size(); i++) {
            count[nums[i]]++;
        }

        for (auto& i: count) {
            res[i.second].push_back(i.first);
        }

        std::vector<int> output;

        for (int i = res.size() - 1; i > 0; i--) {
            for (int j = 0; j < res[i].size(); j++) {
                output.push_back(res[i][j]);
                if (output.size() == k){
                    return output;
                }
            }
        }

    }
};
