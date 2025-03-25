"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/description/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        res = [[1], [1, 1]]

        for i in range(2, numRows):
            row = [1]
            
            for j in range(len(res[i-1]) - 1):
                row.append(res[i-1][j] + res[i-1][j+1])
            
            row.append(1)
            res.append(row)
        
        return res