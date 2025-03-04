import os
import random
import pygame

class Deck:
    def __init__(self):
        self.images = {}
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return None

    def get_backwards_card(self):
        path = os.path.join('static', 'cards', 'blue2.png')
        img = pygame.image.load(path)
        return pygame.transform.scale(img, (117, 167))

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        path = os.path.join('static', 'cards', f'{suit}_{rank}.png')
        self.img = pygame.image.load(path)
        self.img = pygame.transform.scale(self.img, (117, 167))

    def to_string(self):
        return f'[{self.suit}, {self.rank}]'
