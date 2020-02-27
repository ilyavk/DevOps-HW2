import unittest
from deck import Deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
    
    def test_build(self):
        self.deck.build()

    def test_shuffle(self):
        self.deck.shuffle()

    def test_show(self):
        self.deck.show()


if __name__ == "__main__":
    unittest.main()