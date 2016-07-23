class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r>num:
            r = (r+num/r)/2
        return r*r == num
        
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, h = 1, num/2  # l, h = 0, num/2
        while l<h:
            mid = (l+h)/2
            product = mid*mid
            if product == num:
                return True
            elif product < num:
                l = mid + 1
            else:
                h  = mid - 1
        return l*l == num
        
