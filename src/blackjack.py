import pygame
from deck import Deck
from player import Gambler, Dealer
import time

# cards scale will be 117 x 166.5

FELT_COLOR = (53, 101, 77)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def print_state(dealer, gambler, gambler_turn):
    print("Dealers hand", dealer.get_hand(gambler_turn))
    print("Your hand", gambler.get_hand())

def initial_deal(dealer, gambler, screen):
    pygame.display.set_caption("Initial Deal")
    cards = [dealer.deal(gambler), dealer.deal(dealer), dealer.deal(gambler), dealer.deal(dealer)]
    for i in range(len(cards)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return;

        screen.fill(FELT_COLOR)

        xcoords = get_cards_xcoords(2)
        for x in range(i+1):
            ycoord = 10 if x % 2 == 1 else 543
            screen.blit(cards[x].img, (xcoords[x // 2], ycoord))

        pygame.display.flip()
        time.sleep(1)

def gambler_turn(dealer, gambler, screen):
    pygame.display.set_caption("Gambler Turn")
    while gambler.playing():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return;
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    dealer.deal(gambler)
                    time.sleep(1)
                if event.key == pygame.K_s:
                    gambler.stand()
                    time.sleep(1)

        screen.fill(FELT_COLOR)

        dealer_hand = dealer.hand
        dealer_xcoords = get_cards_xcoords(len(dealer_hand))
        for x in range(len(dealer_hand)):
            screen.blit(dealer_hand[x].img, (dealer_xcoords[x], 10))

        gambler_hand = gambler.hand
        gambler_xcoords = get_cards_xcoords(len(gambler_hand))
        for x in range(len(gambler_hand)):
            screen.blit(gambler_hand[x].img, (gambler_xcoords[x], 543))

        pygame.display.flip()
        time.sleep(1)


def get_cards_xcoords(n, card_width=117, margin_width=10):
    total_card_width = n * card_width + (n-1) * margin_width
    center_x = SCREEN_WIDTH // 2
    start_x = center_x - total_card_width // 2
    return [start_x + i * (card_width+margin_width) for i in range(n)]

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dealer = Dealer(Deck())
    gambler = Gambler()

    initial_deal(dealer, gambler, screen)
    gambler_turn(dealer, gambler, screen)

    while gambler.playing():
        choice = ''
        while choice != 's' and choice != 'h':
            choice = input("Stand (s) or Hit (h)")
            if choice == 's':
                gambler.stand()
            elif choice == 'h':
                dealer.deal(gambler)
        print_state(dealer, gambler, True)

    gambler_total = gambler.total()
    if gambler_total > 21:
        print("Bust! Dealer wins")
        return

    print("Dealer Flip")
    print_state(dealer, gambler, False)

    while dealer.total() < 17:
        dealer.deal(dealer)
        print_state(dealer, gambler, False)

    print("Final Hands")
    print_state(dealer, gambler, False)

    dealer_total = dealer.total()

    if dealer_total == gambler_total:
        print("Hands are tied! Push")

    elif dealer_total > gambler_total:
        print("Dealer wins!")

    else:
        print("You Win!")


if __name__ == '__main__':
    main()
