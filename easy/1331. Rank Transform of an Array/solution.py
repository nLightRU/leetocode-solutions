"""
1331. Rank Transform of an Array
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

    Rank is an integer starting from 1.
    The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
    Rank should be as small as possible.

https://leetcode.com/problems/rank-transform-of-an-array/

Input: arr = [40,10,20,30]
Output: [4,1,2,3]

Explanation: 40 is the largest element. 10 is the smallest.

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.

Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
"""

class Solution:
    def create_sorted(self, arr: List[int]) -> List[Dict]:
        res = []
        for i, value in enumerate(arr):
            res.append({'value':  value, 'index': i})
        
        return sorted(res, key=lambda x: x['value'])

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if arr == []:
            return []

        arr_sorted = list(self.create_sorted(arr))
        cur_top = arr_sorted[0]['value'] # current_top
        cur_rank = 1 # current_rank
        
        for elem in arr_sorted:
            value = elem['value']
            index = elem['index']
            if value == cur_top:
                arr[index] = cur_rank
            else:
                cur_top = value
                cur_rank += 1
                arr[index] = cur_rank

        return arr