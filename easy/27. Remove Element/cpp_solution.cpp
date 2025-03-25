class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        size_t val_count = -1;
        for(size_t i = 0; i < nums.size(); ++i){
            if(nums[i] == val) {
                val_count++;
                int tmp = nums[val_count];
                nums[val_count] = nums[i];
                nums[i] = tmp;
            }
        }

        for(size_t i = 0; i < val_count + 1; ++i) {
            nums.erase(nums.begin());
        }

        return nums.size();
    }
};


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int val_count = std::count(nums.begin(), nums.end(), val);

        for(int i = 0; i < val_count; ++i) {
            auto it = std::find(nums.begin(), nums.end(), val);
            nums.erase(it);
        }

        return nums.size();
    }
};