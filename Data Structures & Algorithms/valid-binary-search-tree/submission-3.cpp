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
    bool isValidBST(TreeNode* root) {
        return dfscheck(root, -1001, 1001);
    }

    bool dfscheck(TreeNode* root, long small, long big) {
            if (!root) {
                return true;
            }
            
            if  (!(small < root->val and root->val < big)) {
                return false;
            }

            return dfscheck(root->left, small, root->val) and dfscheck(root->right, root->val, big);
        }
};
