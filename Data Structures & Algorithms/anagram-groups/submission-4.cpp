class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std:: unordered_map <string, vector<string>> result;
        for (int i = 0; i < strs.size(); i++){
            string sortword = strs[i];
            sort(sortword.begin(),sortword.end());
            result[sortword].push_back(strs[i]);
        }
        
        vector<vector<string>> ans;
        for (auto& pair : result){
            ans.push_back(pair.second);
        }

        return ans;
    }
};
