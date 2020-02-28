import unittest
from card import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card("Spades", "Ace")

    def test_show(self):
        self.assertIsNot(self.card.show(), "")

    def test_card_value(self):
        self.assertEqual(self.card.cardValue(), "Ace")

    def test_val(self):
        self.assertNotEqual(self.card.cardValue(), 1)



if __name__ == "__main__":
    unittest.main()