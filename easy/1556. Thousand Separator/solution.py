"""
1556. Thousand Separator
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Input: n = 987
Output: "987"

Example 2:

Input: n = 1234
Output: "1.234"
"""

class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = ''
        pos = 1
        if n < 1000:
            return str(n)
        while n != 0:
            if pos == 0:
                if n > 10:
                    s = '.' + str(n % 10) + s
                else:
                    s = str(n % 10) + s
            else:
                s = str(n % 10) + s
            n //= 10
            pos = (pos + 1) % 3
        return s