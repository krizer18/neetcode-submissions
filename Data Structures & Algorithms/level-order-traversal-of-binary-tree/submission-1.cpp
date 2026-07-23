/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::queue<TreeNode*> myqueue;
        vector<vector<int>> result;
        if (!root) {
            return result;
        }

        myqueue.push(root);

        while (myqueue.size() != 0) {
            vector<int> sublist;
            int quelen = myqueue.size();

            for (int i = 0; i < quelen; i++) {
                TreeNode* value = myqueue.front();
                myqueue.pop();
                if (value) {
                    sublist.push_back(value->val);
                if (value->left){
                    myqueue.push(value->left);
                    }
                if (value->right) {
                    myqueue.push(value->right);
                    }
                }
            }

            result.push_back(sublist);
        }
        return result;
    }
};
