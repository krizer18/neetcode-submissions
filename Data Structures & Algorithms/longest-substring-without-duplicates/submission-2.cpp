class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        std::unordered_set<int> dupset;
        int maxlen = 0;

        for (int r = 0; r < s.size(); r++) {
            while (dupset.contains(s[r])) {
                dupset.erase(s[l]);
                l += 1;
            }
            dupset.insert(s[r]);
            maxlen = std::max(maxlen, r - l + 1);
        }

        return maxlen;
    }
};
