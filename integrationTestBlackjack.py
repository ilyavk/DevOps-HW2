import unittest
from blackjack import Blackjack
from player import Player
from deck import Deck 
from card import Card 

# integration test for Blackjack
class TestBlackJack(unittest.TestCase):

    def setUp(self):
        self.game = Blackjack()

    def test_dealer(self):
        self.assertEqual(self.game.dealer.name, "Dealer")

    def test_gambler(self):
        self.assertEqual(self.game.gambler.name, "Gambler")

    def test_deck(self):
        self.assertNotEqual(self.game.deck, [])

    def test_deal(self):
        self.game.deal()
        self.assertNotEqual(self.game.dealer.hand[0], None)
        self.assertNotEqual(self.game.dealer.hand[1], None)
        self.assertNotEqual(self.game.gambler.hand[0], None)
        self.assertNotEqual(self.game.gambler.hand[1], None)

    def test_total(self):
        self.game.deal()
        self.assertNotEqual(self.game.total(self.game.gambler), 0)

    def test_show_hand(self):
        self.game.deal()
        self.assertIsNone(self.game.showHand(self.game.dealer))

    def test_hit(self):
        self.game.deal()
        self.game.hit(self.game.dealer)
        self.assertIsNotNone(self.game.dealer.hand[2])


if __name__ == "__main__":
    unittest.main()