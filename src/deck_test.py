import unittest
from deck import Deck

class TestDeck(unittest.TestCase):
    def test_deck(self):
        first_deck = Deck()
        second_deck = Deck()

        self.assertEqual(len(first_deck.deck), 52)
        self.assertNotEqual(first_deck.deck, second_deck.deck)
        first_deck.deal()
        self.assertEqual(len(first_deck.deck), 51)

if __name__ == '__main__':
    unittest.main()
