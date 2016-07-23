class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow = 0, 0
        table = collections.defaultdict(set)
        for i, letter in enumerate(secret):
            table[letter].add(i)
            
        tableGuess = collections.defaultdict(set)
        for i, letter in enumerate(guess):
            tableGuess[letter].add(i)
        
        for letter in tableGuess:
            if letter in table:
                correct = table[letter] & tableGuess[letter]
                bull += len(correct)
                cow += min(len(table[letter]), len(tableGuess[letter])) - len(correct)
                
        return str(bull) +"A" +str(cow)+"B"
        
    def getHint(self, secret, guess):
        s, g = collections.Counter(secret), collections.Counter(guess)
        bull = sum( i == j for i, j in zip(secret, guess))
        
        return "%sA%sB" %(bull, sum( (s&g).values()) - bull)
        
    def getHint(self, secret, guess):
        bulls = sum (map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in "0123456789")
        return "%sA%sB" %(bulls, both-bulls)
        

        
