import pygame
from button import Button
from blackjack import play_blackjack

FELT_COLOR = (53, 101, 77)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GAME_MODES = ["Blackjack", "Quit"]

def display_modes(game_modes, screen):
    # calculate where each button should be for it to be centered
    PADDING = 20
    WIDTH, HEIGHT = 300, 60
    X = screen.get_width() // 2
    # need to calc the x, y for each button
    half = len(game_modes) // 2
    y_list = [((i-half) * (PADDING + HEIGHT)) + (screen.get_height() // 2) for i in range(len(game_modes))]
    buttons = []
    for mode, y in zip(game_modes, y_list):
        button = Button(FELT_COLOR, X - (WIDTH // 2), y, WIDTH, HEIGHT, mode)
        buttons.append((mode, button))

    return buttons

def handle_click(buttons, screen):
    for mode, button in buttons:
        if button.isHovering(pygame.mouse.get_pos()):
            match mode:
                case "Blackjack":
                    if not play_blackjack(screen):
                        return False
                    return True
                case "Quit":
                    return False

    return True

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Menu")
    running = True
    font = pygame.font.Font('./static/fonts/Born2bSportyFS.otf', 60)
    quit_index = len(GAME_MODES) - 1
    buttons = display_modes(GAME_MODES, screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = handle_click(buttons, screen)

        screen.fill(FELT_COLOR)

        # starting menu text
        menu_text = font.render("Welcome to my Casino!", True, 'white')
        screen.blit(menu_text, ((SCREEN_WIDTH - menu_text.get_width()) // 2, 30))

        for button in buttons:
            button[1].draw(screen, "white")

        pygame.display.flip()
        
        clock.tick(30)

if __name__ == "__main__":
    main()
