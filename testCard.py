import unittest
from card import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card("Spades", "Ace")

    def test_show(self):
        self.card.show()


if __name__ == "__main__":
    unittest.main()