import pygame

FELT_COLOR = (53, 101, 77)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def centered_coords(obj: pygame.Surface):
    return ((SCREEN_WIDTH - obj.get_width()) // 2, (SCREEN_HEIGHT - obj.get_height()) // 2)

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Menu")
    running = True
    font = pygame.font.Font(None, 60)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(FELT_COLOR)

        # starting menu text
        menu_text = font.render("Welcome to my Casino!", True, 'white')
        screen.blit(menu_text, centered_coords(menu_text))

        pygame.display.flip()
        
        clock.tick(30)

if __name__ == "__main__":
    main()
