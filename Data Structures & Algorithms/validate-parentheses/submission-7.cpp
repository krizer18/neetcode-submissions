class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> bracketmap = {
            {'}', '{'}, 
            {']','['}, 
            {')', '('}
            };
        std::stack<char> tracker;

        for (int i = 0; i < s.length(); i++) {
            if (bracketmap.contains(s[i])) {
                if (tracker.size() == 0) {
                    return false;
                }
                char value = tracker.top();
                tracker.pop();
                if (bracketmap[s[i]] != value) {
                    return false;
                }  
            }
            else {
                tracker.push(s[i]);
            }
        }

        if (tracker.size() > 0) {
            return false;
        }

        return true;
    }
};
