from player import Player
from deck import Deck

class Blackjack:
    def __init__(self):
        self.dealer = Player("Dealer")
        self.gambler = Player("Gambler")
        self.deck = Deck()

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
            elif c.cardValue() == 1:
                total += 11
                if total > 21:
                    total -= 10
            else:
                total += c.cardValue()
        return total

    def showHand(self, person):
        print("-{} holds ".format(person.name))
        person.showHand()

    def hit(self, person):
        person.draw(self.deck)
        print("{} drew {}".format(person.name, person.hand[len(person.hand)-1].val()))

            


if __name__ == "__main__":
    won = False
    while input("Would you like to play Blackjack? (y/n)") == "y":
        game = Blackjack()
        game.deal()
        game.showHand(game.dealer)
        game.showHand(game.gambler)

        print("The dealer has a total of {}".format(game.total(game.dealer)))
        print("The gambler has a total of {}".format(game.total(game.gambler)))

        while input("Does the dealer want to hit? (y/n)") == "y":
            game.hit(game.dealer)
            print("The dealer has a total of {}".format(game.total(game.dealer)))
            if game.total(game.dealer) > 21:
                won = True
                print("Dealer busted. Gambler wins!!")
                break

        while won == False and input("Does the gambler want to hit? (y/n)") == "y":
            game.hit(game.gambler)
            print("The gambler has a total of {}".format(game.total(game.gambler)))
            if game.total(game.gambler) > 21:
                print("Gambler busted. Dealer wins!!")
                break

        # no one busted so highest wins
        if game.total(game.dealer) < 22 and game.total(game.gambler) < 22:
            if game.total(game.dealer) > game.total(game.gambler):
                print("Dealer wins!!")
            elif game.total(game.dealer) < game.total(game.gambler):
                print("Gambler wins!!")
            else:
                print("Gambler and Dealer are tied. House wins!!")

        game.dealer.clearHand()
        game.gambler.clearHand()

    print("Thanks for playing Blackjack ^_^")