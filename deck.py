from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        #self.build()
        #self.show()
        # self.shuffle()

    def build(self):
        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for v in range(1,14): 
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop() # pops a car of the top of the deck
