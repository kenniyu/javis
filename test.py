import card
import combination
#HAVE TO TEST DISCARD PILE


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

print ace, eight, nine, ten, jack, queen, king

pairOfAces = combination.Combination([ace,ace])
straight = combination.Combination([ten,nine,jack,eight,queen])

print pairOfAces
print straight
print pairOfAces.length()
print straight.length()