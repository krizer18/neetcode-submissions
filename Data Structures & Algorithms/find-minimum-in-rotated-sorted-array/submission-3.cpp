class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;

        if (nums[l] < nums[r]){
            return nums[l];
        }

        int res = nums[0];

        while (l <= r) {
            int m = (r - l) / 2 + l;
            res = min(nums[m], res);

            if (nums[m] < nums[r]) {
                r = m - 1;
            }

            else {
                l = m + 1;
            }
        }
        return res;
    }
};