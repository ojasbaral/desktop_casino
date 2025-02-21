from deck import Deck
from player import Gambler, Dealer

def print_state(dealer, gambler, gambler_turn):
    print("Dealers hand", dealer.get_hand(gambler_turn))
    print("Your hand", gambler.get_hand())

def main():
    dealer = Dealer(Deck())
    gambler = Gambler()

    dealer.deal(gambler)
    dealer.deal(dealer)
    dealer.deal(gambler)
    dealer.deal(dealer)
    print("Initial Deal")
    print_state(dealer, gambler, True)

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
