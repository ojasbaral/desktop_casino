import pygame
from deck import Deck
from player import Gambler, Dealer
import time
from button import Button

# cards scale will be 117 x 166.5

FELT_COLOR = (53, 101, 77)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def print_hands(dealer, gambler, screen, gambler_turn):
    backwards_card = dealer.get_backwards_card_img()
    dealer_hand = dealer.hand
    dealer_xcoords = get_cards_xcoords(len(dealer_hand))
    for x in range(len(dealer_hand)):
        if gambler_turn and x == 1:
            screen.blit(backwards_card, (dealer_xcoords[x], 80))
        else:
            screen.blit(dealer_hand[x].img, (dealer_xcoords[x], 80))

    gambler_hand = gambler.hand
    gambler_xcoords = get_cards_xcoords(len(gambler_hand))
    for x in range(len(gambler_hand)):
        screen.blit(gambler_hand[x].img, (gambler_xcoords[x], 493))

def print_ui(screen, gambler):
    font = pygame.font.Font('./static/fonts/Born2bSportyFS.otf', 60)
    smaller_font = pygame.font.Font('./static/fonts/Born2bSportyFS.otf', 30)
    dealer_text = font.render("Dealer's Hand", True, 'white')
    screen.blit(dealer_text, ((SCREEN_WIDTH - dealer_text.get_width()) // 2, 10))
    gambler_text = font.render("Your Hand", True, 'white')
    screen.blit(gambler_text, ((SCREEN_WIDTH - gambler_text.get_width()) // 2, 650))

def initial_deal(dealer, gambler, screen):
    pygame.display.set_caption("Initial Deal")
    cards = [dealer.deal(gambler), dealer.deal(dealer), dealer.deal(gambler), dealer.deal(dealer)]
    backwards_card = dealer.get_backwards_card_img()
    for i in range(len(cards)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False;

        screen.fill(FELT_COLOR)
        print_ui(screen, gambler)
        xcoords = get_cards_xcoords(2)
        for x in range(i+1):
            ycoord = 80 if x % 2 == 1 else 493
            if x == 3:
                screen.blit(backwards_card, (xcoords[x // 2], ycoord))
            else:
                screen.blit(cards[x].img, (xcoords[x // 2], ycoord))

        pygame.display.flip()
        time.sleep(1)

    return True

def gambler_turn(dealer, gambler, screen):
    font = pygame.font.Font('./static/fonts/Born2bSportyFS.otf', 20)
    pygame.display.set_caption("Gambler Turn")
    while gambler.playing():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False;
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    dealer.deal(gambler)
                    time.sleep(1)
                if event.key == pygame.K_s:
                    gambler.stand()
                    time.sleep(1)

        screen.fill(FELT_COLOR)
        print_ui(screen, gambler)
        xcoords = get_cards_xcoords(len(gambler.hand))
        instructions = font.render("hit (h) or stand (s)", True, 'white')
        screen.blit(instructions, ((xcoords[0] - instructions.get_width() - 10), 558))

        print_hands(dealer, gambler, screen, True)

        pygame.display.flip()

    return True

def dealer_flip(dealer, gambler, screen):
    pygame.display.set_caption("Gambler Turn")
    screen.fill(FELT_COLOR)
    print_ui(screen, gambler)
    print_hands(dealer, gambler, screen, False)
    pygame.display.flip()
    time.sleep(1)

def dealer_turn(dealer, gambler, screen):
    pygame.display.set_caption("Dealer Turn")
    while dealer.total() < 17:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False;

        screen.fill(FELT_COLOR)
        print_ui(screen, gambler)
        dealer.deal(dealer)

        print_hands(dealer, gambler, screen, False)

        pygame.display.flip()
        time.sleep(1)

    return True

def display_winner(dealer, gambler, screen, result):
    font = pygame.font.Font('./static/fonts/Born2bSportyFS.otf', 60)
    smaller_font = pygame.font.Font('./static/fonts/Born2bSportyFS.otf', 20)
    pygame.display.set_caption("Game Over")
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 1
                elif event.key == pygame.K_p:
                    return 2

        screen.fill(FELT_COLOR)

        result_text = font.render(result, True, 'white')
        h = (SCREEN_HEIGHT - result_text.get_height()) // 2
        screen.blit(result_text, ((SCREEN_WIDTH - result_text.get_width()) // 2, h - 15))

        opt_text = smaller_font.render("play again (p) or go back to the menu (m)", True, 'white')
        screen.blit(opt_text, ((SCREEN_WIDTH - opt_text.get_width()) // 2, h + 55))


        print_ui(screen, gambler)
        print_hands(dealer, gambler, screen, False)

        pygame.display.flip()


def get_cards_xcoords(n, card_width=117, margin_width=10):
    total_card_width = n * card_width + (n-1) * margin_width
    center_x = SCREEN_WIDTH // 2
    start_x = center_x - total_card_width // 2
    return [start_x + i * (card_width+margin_width) for i in range(n)]

def play_blackjack():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dealer = Dealer(Deck())
    gambler = Gambler()

    if not initial_deal(dealer, gambler, screen): return False
    if not gambler_turn(dealer, gambler, screen): return False

    gambler_total = gambler.total()
    if gambler_total > 21:
        result = "Bust! Dealer wins"

    elif gambler_total == 21:
        dealer_flip(dealer, gambler, screen)
        if dealer.total() == 21:
            result = "Hands are both blackjack! Push!"
        else:
            result = "Blackjack! You win!"

    else:
        dealer_flip(dealer, gambler, screen)
        if not dealer_turn(dealer, gambler, screen): return False
        dealer_total = dealer.total()

        if dealer_total == gambler_total:
            result = "Hands are tied! Push"

        elif dealer_total < 22 and dealer_total > gambler_total:
            result = "Dealer wins!"

        else:
            result = "You Win!"


    res = display_winner(dealer, gambler, screen, result)
    if res == 0: return False
    elif res == 1: return True
    elif res == 2: return play_blackjack()

if __name__ == '__main__':
    play_blackjack()
