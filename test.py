import card
import combination
import discardPile
import history
import player
import rules


""" TESTING CARD / COMBINATION """

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

#print ace, eight, nine, ten, jack, queen, king

pairof3 = combination.Combination([three,three])
pairof4 = combination.Combination([four,four])
pairof5 = combination.Combination([five,five])
pairof6 = combination.Combination([six,six])
pairof7 = combination.Combination([seven,seven])
pairofQ = combination.Combination([queen,queen])
pairofK = combination.Combination([king,king])
pairofA = combination.Combination([ace,ace])
straight = combination.Combination([ten,nine,jack,eight,queen])

print pairofA
#print straight
#print pairOfAces.length()
#print straight.length()

history = history.History()
history.add(pairof3,1)
history.add(pairof5,2)
history.add(pairof7,3)
history.add(pairofQ,4)
history.add(pairofA,1)
print history.list

discard = discardPile.DiscardPile()
discard.add(history)
print "discard:",discard.list

history.clear()
if not history.list:
    print "Passed"

print discard.drawRandomCards(2)
print "discard:",discard.list
#tempHistory
print "__________PLAYER TEST____________"
ken = player.Player("Ken",0)
print "name:",ken.name,"id:",ken.id,"cards:",ken.cards
print ken.addCards([ace,ace,two,two,four,five,six,seven,queen,king,three,three,three])
print ken.addCards([eight])
print "cards:",ken.cards
print "num:",ken.getNumCardsLeft()

print ken.removeCards(["8","2","2"])
print "cards:",ken.cards
print ken.removeCards(["8"])
print "cards:",ken.cards
print "num:",ken.getNumCardsLeft()


