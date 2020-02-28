from player import Player
from deck import Deck

class Blackjack:
    def __init__(self):
        self.dealer = Player("Dealer")
        self.gambler = Player("Gambler")
        self.deck = Deck()
        self.deck.build()
        self.deck.shuffle()

    def deal(self):
        self.dealer.draw(self.deck)
        self.dealer.draw(self.deck)
        self.gambler.draw(self.deck)
        self.gambler.draw(self.deck)

    def total(self, person):
        total = 0
        for c in person.hand:
            if c.cardValue() == 11 or c.cardValue() == 12 or c.cardValue() == 13:
                total += 10
            else:
                total += c.cardValue()
            # have to do something for Ace being 1 or 11
        return total

    def showHand(self, person):
        print("{} holds ".format(person.name))
        person.showHand()

    def hit(self, person):
        person.draw(self.deck)
            


if __name__ == "__main__":
    game = Blackjack()
    game.deal()
    game.showHand(game.dealer)
    game.showHand(game.gambler)
    d_total = game.total(game.dealer)
    print(d_total)
