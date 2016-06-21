"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        occur = set()
        while n != 1:
            sum = 0
            while n > 0 :
                sum += (n%10) * (n%10)
                n /= 10
            n = sum
            if n in occur:
                break
            else:
                occur.add(n)
        return n == 1

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        occur = set()
        while n != 1:
            n = sum([int(i)*int(i) for i in list(str(n))])
            if n in occur:
                break
            occur.add(n)
        return n == 1
        
