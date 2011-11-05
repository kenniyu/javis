class Combination:
    
    def __init__(self, hand):    
        self.hand = sorted( hand, key=lambda x:x.value)
        
    def __repr__(self):
        return "(" + ",".join( map( lambda x:x.name, self.hand) ) + ")"
    
    def length(self):
        return len(self.hand)