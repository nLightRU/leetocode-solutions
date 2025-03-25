func twoSum(nums []int, target int) []int {
    arr := []int{0, 0}
    var flag = false
    for i := 0; i < len(nums) - 1; i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i] + nums[j] == target {
                arr[0] = i;
                arr[1] = j;
                flag = true
                break
            }
        }
        if flag {
            break
        }
    }
    return arr
}