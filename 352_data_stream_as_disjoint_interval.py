# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# this question is similar to longestConsecutive 
# see longest consequtive solutions: https://discuss.leetcode.com/topic/6148/my-really-simple-java-o-n-solution-accepted/2
# and https://discuss.leetcode.com/topic/5333/possibly-shortest-cpp-solution-only-6-lines/3

# this problem solution : best  https://discuss.leetcode.com/topic/47677/java-ac-union-find-solution/2
# addNum: O(1), getInterval: O(nlogn)

#use a vector  https://discuss.leetcode.com/topic/46888/c-solution-using-vector-and-binary-search-with-explanation
# use a vecotor or BST: https://discuss.leetcode.com/topic/46904/very-concise-c-solution

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(int) # boundary number: length
        self.interval = {} # start
        self.intervalList = []  # this can further improve the amortized time complexity of getInterval. avoid repeatedly sorting if no new elements added between calling getInterval 
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if self.map[val]:
            return 
        else:
            self.map[val]  = 1
            
            left = self.map[val-1]
            right = self.map[val+1]
            
            self.map[val-left] = left+right+1
            self.map[val+right] = left+right+1
            
            if right:
                self.interval.pop(val+1, None)

            self.interval[val-left] = val+right
            
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        result = [Interval(start, end) for start,end in self.interval.items()]
        result.sort(key=lambda x: x.start)
        return result
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
