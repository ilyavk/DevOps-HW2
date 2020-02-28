import unittest
from player import Player
from deck import Deck 
from card import Card 

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestPlayer")

    def test_player_name(self):
        self.assertEqual(self.player.name, "TestPlayer")

    def test_empty_hand(self):
        self.assertEqual(self.player.hand, [])

    def test_hand(self):
        self.player.hand.append(Card("Spades", "Ace"))
        self.assertEqual(self.player.hand[0].value, "Ace")

    def test_draw(self):
        self.player.draw(Deck())
        self.assertNotEqual(self.player.hand[0], None)

    def test_show_hand(self):
        self.player.draw(Deck())
        self.assertIsNot(self.player.showHand(), "")

    def test_clear_hand(self):
        self.player.draw(Deck())
        self.player.clearHand()
        self.assertEqual(self.player.hand, [])


if __name__ == "__main__":
    unittest.main()