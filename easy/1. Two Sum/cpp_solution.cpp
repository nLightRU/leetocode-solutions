class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result(2);
        for(int i = 0; i < nums.size() - 1; ++i)
            for(int j = i + 1; j < nums.size(); ++j)
                if(nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }           
        return result;
    }
};