class Rules:
    
    def getType(self,combo):
        
        combolength = len(combo.list)
        
        if combolength == 2 and combo.list[0].name == combo.list[1].name:
            return "pair"
        elif combolength == 5:
            templist = map(lambda x: x.name, combo.list)
            #check for straights
            temp0 = combo.list[0].value
            if combo.list[1].value-temp0==1 and combo.list[2].value-temp0==2 and combo.list[3].value-temp0==3 and combo.list[4].value-temp0==4: 
                return "straight"
            #check for full houses
            temp1 = []
            for val in templist:
                temp1.append(templist.count(val))
            if temp1.count(3) == 3 and temp1.count(2) == 2:
                return "house"
            #check for four of a kind
            temp2 = []
            for val in templist:
                temp2.append(templist.count(val))
            if temp2.count(4) == 4 and temp2.count(1) == 1:
                return "four"
        elif combolength==1:
            return "single"
        return "none"
    
    def compareTo(self,combo1,combo2):
        #assumes lengths are equal
        list1 = map(lambda x: x.value, combo1.list)
        list2 = map(lambda x: x.value, combo2.list)
        if len(combo1.list) != len(combo2.list):
            return None
        elif self.getType(combo1) == "single":
            return list1[0] - list2[0]
        elif self.getType(combo1) == "pair" and self.getType(combo2) == "pair":
            return list1[0] - list2[0]
        elif self.getType(combo1) == "straight" and self.getType(combo2) == "straight":
            temp1 = reduce(lambda x,y : x+y , list1)
            temp2 = reduce(lambda x,y : x+y , list2)
            return temp1 - temp2
        elif self.getType(combo1) == "straight" and self.getType(combo2) == "house":
            return -1
        elif self.getType(combo1) == "straight" and self.getType(combo2) == "four":
            return -1
        elif self.getType(combo1) == "house" and self.getType(combo2) == "straight":
            return 1
        elif self.getType(combo1) == "house" and self.getType(combo2) == "house":
            if list1.count(list1[0]) == 3:
                temp1 = list1[0]
            else:
                temp1 = list1[4]
            if list2.count(list2[0]) == 3:
                temp2 = list2[0]
            else:
                temp2 = list2[4]
            return temp1 - temp2
        elif self.getType(combo1) == "house" and self.getType(combo2) == "four":
            return -1
        elif self.getType(combo1) == "four" and self.getType(combo2) == "straight":
            return 1
        elif self.getType(combo1) == "four" and self.getType(combo2) == "house":
            return 1
        elif self.getType(combo1) == "four" and self.getType(combo2) == "four":
            if list1.count(list1[0]) == 4:
                temp1 = list1[0]
            else:
                temp1 = list1[4]
            if list2.count(list2[0]) == 4:
                temp2 = list2[0]
            else:
                temp2 = list2[4]
            return temp1 - temp2
        else:
            return None