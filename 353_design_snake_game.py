class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        class position:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __hash__(self):
                return hash((self.x, self.y))

            def __eq__(self, other):
                return (self.x, self.y) == (other.x, other.y)

            def __ne__(self, other):
                # Not strictly necessary, but to avoid having both x==y and x!=y
                # True at the same time
                return not(self == other)
                

        # needs to describe the snake position
        startPoint = position(0,0)
        self.body = collections.deque([startPoint])
        self.bodySet = set([startPoint])
        self.width = width
        self.height = height
        self.food = food
        self.foodIndex = 0
        self.score = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        newHead = copy.copy(self.body[-1])
        if direction == 'U':
            newHead.x -= 1
        elif direction == 'D':
            newHead.x += 1
        elif direction == 'L':
            newHead.y -= 1
        elif direction == 'R':
            newHead.y += 1
        headRow = newHead.x
        headCol = newHead.y
        self.bodySet.remove(self.body[0])
        if headRow < 0 or headRow == self.height or headCol < 0 or \
           headCol == self.width or newHead in self.bodySet:
               return -1
            
        self.body.append(newHead)
        self.bodySet.add(newHead)
        
        
        #eat food. keep tail
        if self.foodIndex < len(self.food) and headRow == self.food[self.foodIndex][0] \
           and headCol == self.food[self.foodIndex][1]:
               self.bodySet.add(self.body[0])
               self.score += 1
               self.foodIndex += 1
        else: #regular move. delete tail
            self.body.popleft()
            
        return self.score
                                                                                                                                                                                                                                                                                                           
            
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
