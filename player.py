import util

class Player:
    
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.cards = []
        
    def getNumCardsLeft(self):
        return len(self.cards)
    
    def addCards(self,list):
        self.cards += list
        self.cards = sorted( self.cards , key=lambda x:x.value)
        return list
    
    def removeCards(self,list): #list is a list of CARD NAMES
        templist = map(lambda x: x.name, self.cards)
        for cardName in list:
            if list.count(cardName) > templist.count(cardName): #SEXY use of map and lambda ohhhh shit son
                return False
        temp = []
        for cardToRemove in list:
            for card in self.cards:
                if card.name==cardToRemove:
                    self.cards.remove(card)
                    temp.append(card)
                    continue
        return temp