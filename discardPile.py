import random

class DiscardPile: #NOT TESTED
    
    def __init__(self):
        self.list = []
        
    def add(self,history):
        for combo,id in history.list:
            for card in combo.list:
                self.list.append(card)
                
    def drawRandomCards(self, n):
        random.shuffle(self.list)
        drawn = []
        while ( len(self.list) > 0 and n > 0):
            drawn.append(self.list.pop())
            n-=1
        return drawn
    
    def __repr__(self):
        x = ""
        for card in self.list:
            x= x + card.name + " "
        return x