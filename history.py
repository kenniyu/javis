class History:
    
    def __init__(self):
        self.list = []
        
    def clear(self):
        self.list = []
        
    def add(self, combo, id):
        record = (combo,id)
        self.list.append(record)
        
    def __repr__(self):
        x = ""
        for record in self.list:
            x = x + "{" + str(record[0]) + "," + str(record[1]) + "} "
        return x