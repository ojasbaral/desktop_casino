import unittest
from player import Player, Dealer, Gambler
from deck import Deck, Card

class TestPlayer(unittest.TestCase):
    def test_player(self):
        player = Player()
        player.hand = [Card('hearts', 'ace'), Card('spades', 'jack')]
        self.assertEqual(player.total(), 21)

        player.hand = [Card('hearts', '3'), Card('clubs', '10'), Card('diamonds', '7')]
        self.assertEqual(player.total(), 20)

        player.hand = [Card('spades', 'ace'), Card('diamonds', 'ace'), Card('clubs', '5')]
        self.assertEqual(player.total(), 17)

    def test_dealer(self):
        dealer = Dealer(Deck())
        gambler = Gambler()

        dealer.deal(gambler)
        dealer.deal(dealer)
        self.assertEqual(len(dealer.hand), 1)
        self.assertEqual(len(gambler.hand), 1)

    def test_gambler(self):
        gambler = Gambler()
        gambler.stand()
        self.assertFalse(gambler.playing())

        gambler = Gambler()
        gambler.hand = [Card('hearts', '5'), Card('clubs', '10'), Card('diamonds', '7')]
        self.assertFalse(gambler.playing())

        gambler = Gambler()
        gambler.hand = [Card('hearts', '3'), Card('clubs', '10'), Card('diamonds', '7')]
        self.assertTrue(gambler.playing())

if __name__ == '__main__':
    unittest.main()

