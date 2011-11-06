class Combination:
    
    def __init__(self, hand):    
        self.list = sorted( hand, key=lambda x:x.value)
        
    def __repr__(self):
        return "(" + ",".join( map( lambda x:x.name, self.list) ) + ")"
    
    def length(self):
        return len(self.list)