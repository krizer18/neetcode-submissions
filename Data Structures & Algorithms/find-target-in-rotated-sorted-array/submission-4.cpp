class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) {
            int m = ((r - l) / 2) + l;
            
            if (nums[m] == target) {
                return m;
            }

            else if (nums[m] > nums[r]) {
                if (target < nums[m] and target >= nums[l]) { 
                    r = m - 1;
                }

                else {
                    l = m + 1;
                }
            }

            else { 
                if (target > nums[m] and target <= nums[r]) {
                    l = m + 1;
                }

                else {
                    r = m - 1;
                }
            }
        }
        return -1;
    }
};
