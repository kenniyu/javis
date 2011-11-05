class Card:
    
    def __init__ (self, name, value):
        self.name = name
        self.value = value
    
    def __repr__(self):
#        print self.name,self.value
        x = "[" + self.name + "]"
        return x