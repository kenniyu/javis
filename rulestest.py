import card
import combination
import discardPile
import history
import player
import rules

ace = card.Card("A",14)
two = card.Card("2",15)
three = card.Card("3",3)
four = card.Card("4",4)
five = card.Card("5",5)
six = card.Card("6",6)
seven = card.Card("7",7)
eight = card.Card("8",8)
nine = card.Card("9",9)
ten = card.Card("10",10)
jack = card.Card("J",11)
queen = card.Card("Q",12)
king = card.Card("K",13)

pairof3 = combination.Combination([three,three])
pairof4 = combination.Combination([four,four])
pairof5 = combination.Combination([five,five])
pairof6 = combination.Combination([six,six])
pairof7 = combination.Combination([seven,seven])
pairofQ = combination.Combination([queen,queen])
pairofK = combination.Combination([king,king])
pairofA = combination.Combination([ace,ace])

straight1 = combination.Combination([ten,nine,jack,eight,queen]) #8,9,10,j,q
straight2 = combination.Combination([three,four,five,six,seven])
straight3 = combination.Combination([ten,jack,queen,king,ace])
straight4 = combination.Combination([two,jack,queen,king,ace])

house1 = combination.Combination([ace,ace,ace,two,two]) #A
house2 = combination.Combination([three,three,five,five,three]) #3
house3 = combination.Combination([jack,eight,jack,eight,jack]) #j

four1 = combination.Combination([jack,jack,ace,jack,jack])
four2 = combination.Combination([ace,ace,ace,five,ace])
four3 = combination.Combination([two,three,three,three,three])

fail1 = combination.Combination([ace,queen])
fail2 = combination.Combination([two,four])
fail3 = combination.Combination([three,four,five,six,seven,eight])
fail4 = combination.Combination([two,three,four,five,six])
fail5 = combination.Combination([two,two,three,three,five])
fail6 = combination.Combination([ace,ace,ace,ace,ace])
fail7 = combination.Combination([eight,eight,queen,queen,four])
fail8 = combination.Combination([nine,nine,three,two,ace])

rules = rules.Rules()
print "__________COMPARE TO TEST__________"
print ace, two,rules.compareTo(combination.Combination([ace]),combination.Combination([two]))
print ace, three,rules.compareTo(combination.Combination([ace]),combination.Combination([three]))
print ace, ace,rules.compareTo(combination.Combination([ace]),combination.Combination([ace]))
print " "
print pairof5,pairofQ,rules.compareTo(pairof5,pairofQ)
print pairof5,pairof5,rules.compareTo(pairof5,pairof5)
print pairof5,pairof3,rules.compareTo(pairof5,pairof3)
print pairof5,fail1,rules.compareTo(pairof5,fail1)
print " "
print straight1,straight3,rules.compareTo(straight1,straight3)
print straight1,straight2,rules.compareTo(straight1,straight2)
print straight4,straight4,rules.compareTo(straight4,straight4)
print straight1,fail4,rules.compareTo(straight1,fail4)
print " "
print house3,house1,rules.compareTo(house3,house1)
print house3,house2,rules.compareTo(house3,house2)
print house3,house3,rules.compareTo(house3,house3)
print house3,fail1,rules.compareTo(house3,fail1)
print " "
print four1,four2,rules.compareTo(four1,four2)
print four1,four3,rules.compareTo(four1,four3)
print four1,four1,rules.compareTo(four1,four1)
print four2,fail8,rules.compareTo(four2,fail8)
print " "
print straight1,house1,rules.compareTo(straight1,house1)
print straight1,four1,rules.compareTo(straight1,four1)
print house2,straight2,rules.compareTo(house2,straight2)
print house2,four2,rules.compareTo(house2,four2)
print four3,straight3,rules.compareTo(four3,straight3)
print four3,house3,rules.compareTo(four3,house3)
#print "___________RULES TEST___________"
#print rules.getType(pairofA)
#print rules.getType(pairof3)
#print rules.getType(pairof5)
#print rules.getType(straight1)
#print rules.getType(straight2)
#print rules.getType(straight3)
#print rules.getType(straight4)
#print rules.getType(house1)
#print rules.getType(house2)
#print rules.getType(house3)
#print rules.getType(four1)
#print rules.getType(four2)
#print rules.getType(four3)
#
#print "_________failed test cases__________"
#print rules.getType(fail1)
#print rules.getType(fail2)
#print rules.getType(fail3)
#print rules.getType(fail4)
#print rules.getType(fail5)
#print rules.getType(fail6)
#print rules.getType(fail7)
#print rules.getType(fail8)