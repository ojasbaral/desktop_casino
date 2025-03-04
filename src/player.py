from deck import Deck, Card

class Player:
    def __init__(self):
        self.hand = []

    def take_card(self, card):
        self.hand.append(card)

    def total(self):
        res = 0
        aces = 0
        for card in self.hand:
            if card.rank in ["jack", "queen", "king"]:
                res += 10
            elif card.rank == "ace":
                res += 11
                aces += 1
            else:
                res += int(card.rank)

        while res > 21 and aces > 0:
            res -= 10
            aces -= 1

        return res

class Dealer(Player):
    def __init__(self, deck: Deck):
        super().__init__()
        self.deck = deck

    def deal(self, player):
        card = self.deck.deal()
        player.take_card(card)
        return card

    def get_hand(self, gambler_turn):
        res = []
        if gambler_turn:
            res.append(['[*, *]'])
            for card in self.hand[1:]:
                res.append(card.to_string())
        else:
            for card in self.hand:
                res.append(card.to_string())

        return res
    
    def get_backwards_card_img(self):
        return self.deck.get_backwards_card()

class Gambler(Player):
    def __init__(self):
        super().__init__()
        self.is_stand = False

    def take_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        res = []
        for card in self.hand:
            res.append(card.to_string())

        return res

    def stand(self):
        self.is_stand = True

    def playing(self):
        total = self.total()
        if total >= 21 or self.is_stand:
            return False

        return True

