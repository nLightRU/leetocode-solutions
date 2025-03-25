"""
14. Longest Common Prefix

https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

tests:
["flower","flow","flight"] - 'fl'
["dog","racecar","car"] - ''
["",""] - '
["ab", "a"] - 'a'

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:               
        pref = strs[0]
        if '' in strs:
            return ''

        for i in range(1, len(strs)):
            j = 0
            min_len = min(len(pref), len(strs[i]))
            while pref[j] == strs[i][j] and j < min_len:
                j += 1
                if j == min_len:
                    break

            pref = pref[:j]
            if not pref:
                return pref

        return pref