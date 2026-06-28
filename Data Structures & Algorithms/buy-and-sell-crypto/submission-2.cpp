class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxp = 0;
        int l = 0;
        int r = 0;

        while (r < prices.size()) {
            if (prices[l] > prices[r]) {
                l = r;
                r += 1;
            }

            else {
                int profit = prices[r] - prices[l];
                maxp = std::max(profit, maxp);
                r += 1;
            }
        }
    return maxp;
    }
};
