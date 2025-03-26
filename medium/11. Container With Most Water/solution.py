
# min_h * r

"""
https://leetcode.com/articles/two-pointer-technique/
https://wcademy.ru/two-pointers-method/
https://www.geeksforgeeks.org/two-pointers-technique/
 [1,8,6,2,5,4,8,3,7]
[1,1]
[9384,887,2778,6916,7794,8336,5387,493,6650,1422,2363,28,8691,60,7764,3927,541,3427,9173,5737,5212,5369,2568,6430,5783,1531,2863,5124,4068,3136,3930,9803,4023,3059,3070,8168,1394,8457,5012,8043,6230,7374,4422,4920,3785,8538,5199,4325,8316,4371,6414,3527,6092,8981,9957,1874,6863,9171,6997,7282,2306,926,7085,6328,337,6506,847,1730,1314,5858,6125,3896,9583,546,8815,3368,5435,365,4044,3751,1088,6809,7277,7179]
[8,7,2,1]
[1,2,3,1000,9]
"""

# Пока не работает (проходит частично)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])

        def count_v(left, right, height):
            return (right - left) * min(height[left], height[right])

        # может если минимальный правее середниы,
        # то если меньше, то двигать левую? (что я понял из хинта)
        # т.е. надо менять переврнуть условие, когда сдвигаем

        min_height_i = 0
        for i in range(1, len(height)):
            if height[i] < height[min_height_i]:
                min_height_i = i

        min_on_left = False if min_height_i > len(height) // 2 else True
        # change_shift = False

        left = 0
        right = len(height) - 1
        max_v = min(height[0], height[-1]) * (len(height) - 1)

        while left != right:
            v = count_v(left, right, height)
            if v < max_v:
                left += 1
            elif v > max_v:
                max_v = v
                right -= 1
            else:
                if min_on_left:
                    left += 1
                else:
                    right -= 1                
        return max_v