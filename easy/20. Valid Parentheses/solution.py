"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

inputs:
    "(){}}{"
    "(]"
    "()[]{}"
    "()"    

"""

class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        stack = [s[0]]
        for cur in s[1:]:
            if cur in ('(', '[', '{'):
                stack.append(cur)
            else:
                if not stack:
                    stack.append(cur)
                    continue
                elif stack[-1] == pairs[cur]:
                    stack.pop()
                    continue
                else:
                    stack.append(cur)
        
        return True if not stack else False