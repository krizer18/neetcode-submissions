class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maxa = 0;
        int l = 0;
        int r = heights.size() - 1;
        
        while (l < r){
            int area = std::min(heights[l], heights[r]) * (r - l);
            maxa = std::max(area, maxa);

            if (heights[l] < heights[r]) {
                l += 1;
            }
            else if (heights[r] < heights[l]) { 
                r -= 1;
            }
            else{
                l += 1;
            }
        }
        return maxa;
    }
};
