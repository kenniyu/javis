import random

class DiscardPile: #NOT TESTED
    
    def __init__(self):
        self.cards = []
        
    def add(self,history):
        for hand in history:
            for card in hand[0]:
                self.card.append(card)
                
    def drawRandomCards(self, n):
        random.shuffle(self.cards)
        drawn = []
        while ( len(self.cards) > 0 and n > 0):
            drawn.append(self.cards.pop())
            n-=1
        return drawn